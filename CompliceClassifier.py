__author__ = 'Brian Stock - bestock@uwaterloo.ca'

from TaskParser import TaskParser
from sklearn.cross_validation import train_test_split
from scipy import io
import numpy as np
import re

tp = TaskParser()
task_description_list = tp.task_description_list
task_completed_list = tp.task_complete_list
word_set = tp.wordset
word_counter = tp.c

#print word_set

# Combine task_description_list and task_completed_list into a list of tuples.
task_data = zip(task_description_list, task_completed_list)
# Split data into training and test data (70/30 split).
train_data, test_data = train_test_split(task_data, train_size=0.7)
# Unzip training and test data.
train_task_descriptions, train_task_labels = zip(*train_data)
test_task_descriptions, test_task_labels = zip(*test_data)

# Build dataset for number of words in a task.
train_wordcount_data = []
for task in train_data:
    train_wordcount_data.append(len(re.findall(r'\w+', task[0])))  # count number of words in task description
test_wordcount_data = []
for task in test_data:
    test_wordcount_data.append(len(re.findall(r'\w+', task[0])))  # count number of words in task description

top_words = tp.c.most_common(200)
# Extract number of specific number words used for top 200 words.
train_top_wordcounts = []
test_top_wordcounts = []
for top_word in top_words:
    word_string = top_word[0]
    train_top_wordcounts.append([])
    for task_description in train_task_descriptions:
        train_top_wordcounts[-1].append([])
        train_top_wordcounts[-1][-1] = task_description.count(word_string)
    test_top_wordcounts.append([])
    for task_description in test_task_descriptions:
        test_top_wordcounts[-1].append([])
        test_top_wordcounts[-1][-1] = task_description.count(word_string)

# Export extracted features to MATLAB data file.
io.savemat('train_data.mat', {'train_task_descriptions': train_task_descriptions, 'train_task_labels': train_task_labels,
                              'train_wordcount_data': train_wordcount_data, 'train_top_wordcounts': train_top_wordcounts})
io.savemat('test_data.mat', {'test_task_descriptions': test_task_descriptions, 'test_task_labels': test_task_labels,
                             'test_wordcount_data': test_wordcount_data, 'test_top_wordcounts': test_top_wordcounts})

# Train network with dataset, for number of words in a task.
#net = nl.net.newff([[min(min(test_wordcount_data), min(train_wordcount_data)), max(max(test_wordcount_data), max(train_wordcount_data))]], [1, 1])

#training_error = net.train(train_wordcount_data, train_task_labels, show=1)
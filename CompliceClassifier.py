__author__ = 'Brian Stock - bestock@uwaterloo.ca'

from TaskParser import TaskParser
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import re

tp = TaskParser()
task_description_list = tp.task_description_list
task_completed_list = tp.task_complete_list
word_set = tp.wordset
word_counter = tp.c

print word_set

# Build dataset for number of words in a task.
n_words_dataset = SupervisedDataSet(1, 1)
for idx, task_description in enumerate(task_description_list):
    count = len(re.findall(r'\w+', task_description))  # count number of words in task description
    n_words_dataset.addSample(count, task_completed_list[idx])

# Build network for number of words in a task.
net = buildNetwork(1, 20, 1)

# Train network with dataset, for number of words in a task.
n_words_trainer = BackpropTrainer(net, n_words_dataset)
training_error = n_words_trainer.train()
print training_error
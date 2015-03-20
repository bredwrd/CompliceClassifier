__author__ = 'Brian Stock - bestock@uwaterloo.ca'

import csv
import re
from collections import Counter

tasks_data_file = open('Resources/taskstats_1422603158567.csv')
tasks_data = csv.reader(tasks_data_file)

task_list = []

task_description_list = []  # String describing a task
task_complete_list = []  # Task completed? True or False

re_pattern = '^([^>+])?(-?)(\d|[A-Z]{2}).{0,3}?([\)\]]+) ? *?(.*)'

wordset = set()
wordlist = []
worDic = {}

c = Counter()

for task_row in tasks_data:
    # Split rows based on linebreak symbol '#####'
    task_row = task_row[3].split('#####')

    for task_cell in task_row:
        # Filter individual tasks based on regex: ^([^>+])?(-?)(\d|[A-Z]{2}).{0,3}?([\)\]]+) ? *?(.*)
        task_match = re.match(re_pattern, task_cell)
        if task_match:
            # Append description.
            task_description = task_match.group(5)
            task_description_list.append(task_description)
            # Append complete (True or False).
            task_incomplete_flag = task_match.group(1)  # '-' if incomptete, 'None' if complete
            if task_incomplete_flag == '-':
                task_complete_list.append(False)
            else:
                task_complete_list.append(True)

            # print task_incomplete_flag
            # print task_description

            words = re.sub("[^\w]", " ",  task_match.group(5).lower()).split()
            c.update(words)
            for word in words:
                wordlist.append(word)
                wordset.add(word)
                # print word
                # worDic[word] = (worDic.get(word, False)+1) if worDic.get(word, False) else 1

print '===================== 4930 words used >=2 times'
print '===================== 3600 words used >=3 times'
print '===================== 2900 words used >=4 times'
print c.most_common(500)
# c = Counter(wordlist)

# print wordset
print len(wordset)
print "len(wordlist)"
print len(wordlist)
# print "len(worDic)"
# print len(worDic)

# print task_description_list[0]
# print task_complete_list[0]

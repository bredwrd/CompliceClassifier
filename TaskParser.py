__author__ = 'Brian Stock - bestock@uwaterloo.ca'

import csv
import re
from collections import Counter


class TaskParser:
    def __init__(self):
        tasks_data_file = open('Resources/taskstats_1422603158567.csv')
        tasks_data = csv.reader(tasks_data_file)

        self.task_description_list = []  # String describing a task
        self.task_complete_list = []  # Task completed? True or False

        re_pattern = '^([^>+])?(-?)(\d|[A-Z]{2}).{0,3}?([\)\]]+) ? *?(.*)'

        wordset = set()
        wordlist = []
        worDic = {}
        c = Counter()

        for task_row in tasks_data:
            # Split rows based on linebreak symbol '#####'
            task_row = task_row[3].split('#####')

            for task_cell in task_row:
                # Filter individual tasks based on regex pattern.
                task_match = re.match(re_pattern, task_cell)
                if task_match:
                    # Append description.
                    task_description = task_match.group(5)
                    self.task_description_list.append(task_description)
                    # Append complete (True or False).
                    task_incomplete_flag = task_match.group(1)  # '-' if incomptete, 'None' if complete
                    if task_incomplete_flag == '-':
                        self.task_complete_list.append(False)
                    else:
                        self.task_complete_list.append(True)

                    words = re.sub("[^\w]", " ",  task_match.group(5).lower()).split()
                    c.update(words)
                    for word in words:
                        wordlist.append(word)
                        wordset.add(word)

        print '===================== 4930 words used >=2 times'
        print '===================== 3600 words used >=3 times'
        print '===================== 2900 words used >=4 times'
        print c.most_common(500);
        print 'total words:'
        print len(wordset)

    def get_description_list(self):
        return self.task_description_list

    def get_completed_list(self):
        return self.task_complete_list
__author__ = 'Brian Stock - bestock@uwaterloo.ca'

import csv
import re


class TaskParser:
    def __init__(self):
        tasks_data_file = open('Resources/taskstats_1422603158567.csv')
        tasks_data = csv.reader(tasks_data_file)

        self.task_description_list = []  # String describing a task
        self.task_complete_list = []  # Task completed? True or False

        re_pattern = '^([^>+])?(-?)(\d|[A-Z]{2}).{0,3}?([\)\]]+) ? *?(.*)'

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

    def get_description_list(self):
        return self.task_description_list

    def get_completed_list(self):
        return self.task_complete_list
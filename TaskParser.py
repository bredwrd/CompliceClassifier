__author__ = 'Brian Stock - bestock@uwaterloo.ca'

import csv
import re

tasks_data_file = open('Resources/taskstats_1422603158567.csv')
tasks_data = csv.reader(tasks_data_file)

task_list = []

task_description_list = []  # String describing a task
task_complete_list = []  # Task completed? True or False

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
            task_description_list.append(task_description)
            # Append complete (True or False).
            task_incomplete_flag = task_match.group(1)  # '-' if incomptete, 'None' if complete
            if task_incomplete_flag == '-':
                task_complete_list.append(False)
            else:
                task_complete_list.append(True)

            print task_description
            print task_incomplete_flag
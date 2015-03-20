__author__ = 'Brian'

import csv

goals_data_file = open('Resources/taskstats_1422603158567.csv')
goals_data = csv.reader(goals_data_file)

goal_list = []

for row in goals_data:
    # Split rows based on linebreak symbol '#####'
    goal_row = row[3].split('#####')

    # Remove first element of split row if not meaningful.
    if goal_row == '' or goal_row == 'undefined':
        goal_row.pop(0)
    goal_list = goal_list + goal_row  # Add new row of goals to list of goals.

print goal_list
__author__ = 'Brian'

import csv

goals_data_file = open('Resources/taskstats_1422603158567.csv')
goals_data = csv.reader(goals_data_file)

goal_list_list = []

for row in goals_data:
    goal_list_list.append(row[3])

print goal_list_list
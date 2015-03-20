__author__ = 'Brian Stock - bestock@uwaterloo.ca'

from TaskParser import TaskParser

tp = TaskParser()
task_description_list = tp.get_description_list()
task_completed_list = tp.get_description_list()

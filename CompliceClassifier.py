__author__ = 'Brian Stock - bestock@uwaterloo.ca'

from TaskParser import TaskParser
from pybrain.tools.shortcuts import buildNetwork

tp = TaskParser()
task_description_list = tp.task_description_list
task_completed_list = tp.task_complete_list
word_set = tp.wordset
word_counter = tp.c

print word_set
# -*- coding: utf-8 -*-
"""apache beam 1 marchipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RRZXb17N2OQiRY3Cqs1U28ApREs7OpRm
"""

# Run and print a shell command.
def run(cmd):
  print('>> {}'.format(cmd))
  !{cmd}
  print('')

# Install apache-beam.
run('pip install --quiet apache-beam')

from google.colab import files
uploaded = files.upload()

run('ls')

import apache_beam as beam

p1 = beam.Pipeline()

def SplitRow(element):
    return element.split(',')

def filtering(record):
  return record[3] == 'Accounts'

attendance_count = (
    p1
    |beam.io.ReadFromText('dept_data.txt')
    |beam.Map(SplitRow)
    |beam.Filter(filtering)
    |beam.Map(lambda record: (record[1], 1))
    |beam.CombinePerKey(sum)
    |beam.io.WriteToText('output_new_final')
)

p1.run()

# Sample the first 20 results, remember there are no ordering guarantees.
run('head -n 20 output_new_final-00000-of-00001')


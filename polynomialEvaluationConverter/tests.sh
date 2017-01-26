#!/bin/sh

#  Run tests
#
#  simple script to run tests and reset data
#
#
#

cp testDataCopy.csv testData.csv
# resets the input file
python3 polyEvalStrings.py --source_filename testData.csv
# runs the conversion code on the tests
vim testData.csv
# displays the test results
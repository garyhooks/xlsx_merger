############################################################################
#
# Combine several shreadsheets or CSV into a database
# Extract then into CSV file to combine all data into one worksheet
#
# Author: Gary Hooks
# Date of Release: 16th February 2018
# Licence: GPL
#
# USAGE:
# 1) Use SQLite to create database with the column names outputted here
# 2) Set each column type to "TEXT" - even if it's a number!
############################################################################

import os
import csv
import sys
import sqlite3

def columnCheck(columns, name):

    if not name in columns:
        return 0
    else:
        return 1

def main():

    ## Where is your SQL Lite Database...
    __DB__ = "C:\\route\\to\\sqlite\\database.db"

    ## Attempt to connect to DB
    try:
        conn = sqlite3.connect(__DB__)
    except:
        sys.exit("ERROR: Can't connect to database")

    ## Make columns list ready to save each name into
    columns = []

    ## Where are all the spreadsheets that you want to combine...
    directory = "C:\\route\\to\\your\\spreadsheets"

    ## Loop through all the files in this directory
    for file in os.listdir(directory):

        myfile = directory + "\\" + file

        ## Open each file for reading
        with open(myfile, "r") as myfile:

            ## Read in each of the rows here...
            csvreader = csv.reader(myfile, dialect="excel")
            counter = 0

            ## Go through each row in the sheet
            for row in csvreader:

                    colNumber = 0

                    ## Now loop through each column within that row
                    for col in row:

                        ## if counter == 0 ... that means we are at the VERY TOP of the sheet and this is the headings
                        if counter==0:

                                ## Now we have the column name... check if it exists in our list...
                                ## if it doesnt (0) add it
                                if columnCheck(columns, col) == 0:
                                    columns.append(col)
                                    colNumber+=1
                    counter += 1


    for name in columns:
        print(name)


if __name__ == "__main__":
    main()
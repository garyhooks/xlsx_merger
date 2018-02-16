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
# 1) Set variable __DB__ to the database you previously created
# 2) Set directory to the path of where all your spreadsheets are
############################################################################

import os
import csv
import sys
import sqlite3

def main():

    __DB__ = "C:\\Route\\to\\your\\database.db"

    try:
        conn = sqlite3.connect(__DB__)
        c = conn.cursor()
    except:
        sys.exit("ERROR: Can't connect to database or set up a cursor")


    # Get all the files from directory
    directory = "C:\\Route\\to\\your\\spreadsheets"

    for file in os.listdir(directory):

        myfile = directory + "\\" + file
        print(myfile)

        with open(myfile, "r") as myfile:

            columns = []

            ## Read in each of the rows here...
            csvreader = csv.reader(myfile, dialect="excel")
            counter = 0
            startSQL = "INSERT INTO data ("

            for row in csvreader:
                sql = ""

                colcount = 1
                for col in row:

                    if counter == 0:
                        #print(row)
                        columns.append(col)
                    else:
                        if colcount == len(row):
                            sql += "'" + col + "')"
                        else:
                            sql += "'" + col + "', "

                    colcount+=1


                if counter == 0:
                    numberOfColumns = columns.__len__()
                    i = 1
                    for colName in columns:
                        if i == numberOfColumns:
                            startSQL += colName + ") VALUES ("
                        else:
                            startSQL += colName + ", "

                        i+=1

                else:

                    c.execute(startSQL + sql)
                    conn.commit()

                counter += 1

            counter += 1

if __name__ == "__main__":
    main()
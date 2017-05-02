import cx_Oracle
import csv

con = cx_Oracle.connect('connection info goes here')

with open('csv file', 'rb') as csvfile: #this opens up a csv list with lines for the query
    reader = csv.reader(csvfile, delimiter=',')
    with open('', 'w') as newfile: #creates the new list we'll make with the results of the query


        #I had two queries because my list sometimes had data for a field, and sometimes it didn't, 
        #but I wanted to use it if it did 
        query1 = """
        """

        query2 = """
        """

        for row in reader:
            if row[2] !=' ':
 
                cur = con.cursor()
                cur.execute(query1, (row[3], row[1], row[2] + '%'))

                results = cur.fetchall()

                newfile.write(row[0])
                newfile.write(',')
                newfile.write(row[1])
                newfile.write(',')
                newfile.write(row[2])
                newfile.write(',')
                newfile.write(row[3])
                newfile.write(',')
                newfile.write(row[4])
                for i in results:
                    newfile.write(',')
                    newfile.write(i[0])

                newfile.write('\n')
 
            else:

                cur = con.cursor()
                cur.execute(query2, (row[3], row[1]))

                results = cur.fetchall()

                newfile.write(row[0])
                newfile.write(',')
                newfile.write(row[1])
                newfile.write(',')
                newfile.write(row[2])
                newfile.write(',')
                newfile.write(row[3])
                newfile.write(',')
                newfile.write(row[4])
                for i in results:
                    newfile.write(',')
                    newfile.write(i[0])

                newfile.write('\n')


con.close()

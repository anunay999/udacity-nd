"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
count = set()
with open('texts.csv', 'r') as t,open('calls.csv', 'r') as c:
    reader_t = csv.reader(t)
    texts = list(reader_t)
    reader_c = csv.reader(c)
    calls = list(reader_c)
    for text,call in zip(texts,calls):
        count.add(text[0])
        count.add(text[1])
        count.add(call[0])
        count.add(call[1])
        
        


print("There are",str(len(count)),"different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

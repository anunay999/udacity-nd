"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
        
"""with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
"""
def get_call_time_by_phone(calls):
    phn_dict = {}
    for record in calls:
        if(record[0] in phn_dict.keys()):
            phn_dict[record[0]]+=int(record[3])
        else:
            phn_dict[record[0]]=int(record[3])
        if(record[1] in phn_dict.keys()):
            phn_dict[record[1]]+=int(record[3])
        else:
            phn_dict[record[1]]=int(record[3])        
    return phn_dict

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    records = get_call_time_by_phone(calls)
    phone_number = max(records,key = records.get)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number,records[phone_number]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


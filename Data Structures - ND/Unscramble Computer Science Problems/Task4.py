"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
def get_phone_numbers(texts,calls):
    count = set()
    phone_dict={}
    for i,j in zip(texts,calls):
        if i[0] in phone_dict.keys():
            phone_dict[i[0]]['out_text']=1
        else:
            phone_dict[i[0]] = {'out_text':1}
        if j[0] in phone_dict.keys():
            phone_dict[j[0]]['out_call']=1
        else:
            phone_dict[j[0]] = {'out_call':1}
        
        if i[1] in phone_dict.keys():
            phone_dict[i[1]]['in_text']=1
        else:
            phone_dict[i[1]] = {'in_text':1}
        if j[1] in phone_dict.keys():
            phone_dict[j[1]]['in_call']=1
        else:
            phone_dict[j[1]] = {'in_call':1}
        #count.add(j[0])
        #count.add(j[1])
    return phone_dict

def get_number_not_in_records(phone_numbers):
    telemarketers = []
    for number in phone_numbers.keys():
        if(len(phone_numbers[number])==1):
            if 'out_call' in phone_numbers[number].keys():
                telemarketers.append(number)
    return telemarketers
            
        
with open('texts.csv', 'r') as t,open('calls.csv', 'r') as c:
    reader_t = csv.reader(t)
    texts = list(reader_t)
    reader_c = csv.reader(c)
    calls = list(reader_c)
    phone_numbers = get_phone_numbers(texts,calls)
    records = get_number_not_in_records(phone_numbers)
    records.sort()
    print("These numbers could be telemarketers: ",)
    for number in records:
        print(number)
    

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

def extract_code(number):
    if '140' in number[:3]:
        return '140'
    elif number[0] in ['7','8','9']:
        return number[:4]
    elif re.search("^([0-9]*)[0-9]*",number):
        fixed_line = number[number.find("(")+1:number.find(")")]
        return fixed_line
    return False

def is_bangalore(number):
    return number[:5]=='(080)' #(080)
    
                             
def get_area_codes(calls):
    area_codes = set()
    count_bangalore_in = 0
    count_bangalore_out = 0    
    for record in calls:
        call_out=record[0]
        call_in=record[1]
        if is_bangalore(call_out):
            area_code = extract_code(call_in)
            if area_code:
                area_codes.add(area_code)
                count_bangalore_out+=1
                if(is_bangalore(call_in)):
                    count_bangalore_in+=1
    return area_codes,count_bangalore_in,count_bangalore_out   
        
with open('calls.csv', 'r') as c:
    reader = csv.reader(c)
    calls = list(reader)
    area_codes,total_in,total_out = get_area_codes(calls)
    codes =  list(area_codes)
    codes.sort(key=str)
    print("The numbers called by people in Bangalore have codes:")
    for code in codes:
        print(code)
    percentage = (total_in/total_out)*100
    print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."%(percentage))
    
    
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
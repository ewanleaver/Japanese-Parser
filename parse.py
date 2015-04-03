#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

input_list=[];
output_list=[];

i=1

while True:
    input_str = raw_input(">")
    if input_str == "Created with Japanese for iOS®":
        break
    else:
        if ((input_str != '') and not (input_str[0].isalpha())):
            input_item = [];
            print("\n" + str(i) + " " + input_str)
            #input_item.append(str(i))
            input_item.append(input_str)
           
            while (input_str != ''):
                input_str = raw_input(">")
		if ((input_str != '') and (input_str[0].isalpha() or (input_str[0] == '\x28'))):
                    input_item.append(input_str)

            input_list.append(input_item)
            i += 1

print(input_list)

random.shuffle(input_list) # << shuffle before print or assignment

# Expand each item in the list
for item in input_list:
	output_list.append('\n'.join(item))

# Expand entire list
with open("output.txt", "w") as myfile:
	myfile.write('\n\n'.join(output_list))

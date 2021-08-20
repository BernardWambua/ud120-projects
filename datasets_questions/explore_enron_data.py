#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py <input> <output>
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
count = 0
for person in enron_data:
    if enron_data[person]["poi"]==1 and enron_data[person]['total_payments'] != 'NaN':
        count += 1
# print(count)
# print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
# print(enron_data["SKILLING JEFFREY K"]["total_payments"])
# print(enron_data["LAY KENNETH L"]["total_payments"])
# print(enron_data["FASTOW ANDREW S"]["total_payments"])
# print(enron_data)
count2 = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        count2 += 1
print(count2)
##############################SKILLING JEFFREY K##########################################################
# lines = []
# with open("../final_project/poi_names.txt") as f:
#     lines = f.readlines()
# lines = lines[2:]
# poi = []
# for item in lines:
#     item = item[4:]
#     item = item[:-1]
#     item = item.lower()
#     poi.append(str(item.replace(",", "")))
# print(len(poi))

# enron_data_keys = list(enron_data.keys())
# print(enron_data_keys)
# poi_in_data = []
# count3=0
# for name in enron_data_keys:
#     if name.lower() in poi:
#         poi_in_data.append(name)
#         if enron_data[name]['total_payments'] != 'NaN':
#             count3+=1
# print(poi_in_data)
# print(count3)
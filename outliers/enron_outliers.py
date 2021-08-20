#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
sys.path.append("../")
from feature_format import featureFormat, targetFeatureSplit
from str_to_bytes import StrToBytes


### read in data dictionary, convert to numpy array
data_dict = pickle.load(StrToBytes(open("../final_project/final_project_dataset.pkl", "r") ) )

data_dict.pop('TOTAL', 0)

features = ["salary", "exercised_stock_options"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

key_to_be_deleted = 'NaN'
for person in data_dict.copy():
    if data_dict[person]['salary'] == key_to_be_deleted:
        data_dict.pop(person)
# for person in data_dict.copy():      
#     if data_dict[person]['bonus'] == key_to_be_deleted:
#         data_dict.pop(person)
print(sorted(data_dict,key=lambda x:int(data_dict[x]['salary'])))
print(data_dict['BANNANTINE JAMES M']['salary'])
print(data_dict['SKILLING JEFFREY K']['salary'])

# print(sorted(data_dict,key=lambda x:int(data_dict[x]['bonus'])))


# matplotlib.pyplot.xlabel("salary")
# matplotlib.pyplot.ylabel("bonus")
# matplotlib.pyplot.show()
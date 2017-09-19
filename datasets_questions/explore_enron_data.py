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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))



# Print the length og the enron dataset
print "The length of the Enron Dataset is: ", len(enron_data)

# For each person, how many features are available?
print "Total number of features available for each person: ", len(enron_data["SKILLING JEFFREY K"])

# How many POIs are there in the E+F dataset?
def find_no_of_POI(data_set):
    no_of_POI = []
    for key, value in data_set.iteritems():
        if value["poi"]==1:
            no_of_POI.append(value)
    return len(no_of_POI)

print "Number POI's identified in dataset: ",find_no_of_POI(enron_data)

# How many POIs are there in total in the text file?
def read_poi_names():
    no_of_names = []
    # Reading the file using the 'with' keyword
    with open('../final_project/poi_names.txt', 'r') as f:
        for line in f:
            no_of_names.append(line.strip())
    # removing the empty space and the link on the first line
    for i in range(2):
        del no_of_names[0]
    return no_of_names

print "Total Number POI's present: ", len(read_poi_names())

#What is the total value of the stock belonging to James Prentice?
print "Total value of the stock belonging to James Prentice: ", enron_data['PRENTICE JAMES']['total_stock_value']

#How many email messages do we have from Wesley Colwell to persons of interest?
print "Number of email messages we have from Wesley Colwell to persons of interest: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#What the value of stock options exercised by Jeffrey K Skilling?
print "Total value of stock options exercised by Jeffrey K Skilling: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# CEO of Enron
print("CEO of Enron: LAY KENNETH L")
# Chairman of Enron
print("Chairman of Enron: SKILLING JEFFREY K")
# CFO of Enron
print("Chairman of Enron: FASTOW ANDREW S")
#Of these three individuals (Lay, Skilling and Fastow), who took home the most money?
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

#How many folks in this dataset have a quantified salary? What about a known email address?
def find_quantified_salary(data_set, entity):
    result_set = []
    for key, value in data_set.iteritems():
        if value[entity] != 'NaN':
            result_set.append(value)
    return len(result_set)

print "Number Quantified salary holders identified in dataset: ",find_quantified_salary(enron_data, "salary")
print "Number Quantified salary holders with email id identified in dataset: ",find_quantified_salary(enron_data, "email_address")
no_of_people_without_pay = len(enron_data) - find_quantified_salary(enron_data, "salary")
# How many people in the E+F dataset have NaN for their total payments?
print "Number of people in the E+F dataset have NaN for their total payments: ", no_of_people_without_pay
# What percentage of people in the dataset as a whole is this?
print "percentage of people in the E+F dataset have NaN for their total payments: ", no_of_people_without_pay
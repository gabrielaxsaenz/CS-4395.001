'''
Author: Gabriela Saenz
CS 4395.001
Fall 2022 @ University of Texas at Dallas
Portfolio Assignment 1
'''


import sys
import os
import re
import pickle

class Person:

    def __init__(self, last, first, mi, id, phone):
        self.lastName = last
        self.firstName = first
        self.middle = mi
        self.employeeID = id
        self.phoneNum = phone

    def display(self):
        print(f'Employee id: {self.employeeID}')
        print(f'\t{self.firstName} {self.middle} {self.lastName}')
        print(f'\t{self.phoneNum}')


def process_txt(txt):
    personDict = {}
    tokens = txt.split('\n') #split file on new line to separate each person's data'
    data = tokens[1:] #start at index 1, ignore header line
    #Process Data for each person
    for d in data[0:]:
        d = d.split(',')
        #Assign the data to the proper token in the text
        fName = d[0]
        lName = d[1]
        mid = d[2]
        eID = d[3]
        pNum = d[4]
        fName = fName[0].upper() + fName[1:].lower()
        lName = lName[0].upper() + lName[1:].lower()
        if not mid:
            mid = 'X'
        else:
            mid = mid[0].upper()

        eIDMatch = re.search("^[A-Za-z]{2}\d{4}$", eID)
        if eIDMatch:
            eID = eID[0:2].upper() + eID[2:]
        else:
            while not eIDMatch:
                print(f"ID is invalid: {eID}")
                print(f'ID is two letter followed by 4 digits')
                neweID = input("Please enter a valid id: ")
                eIDMatch = re.search("^[A-Za-z]{2}\d{4}$", neweID)
            eID = neweID[0:2].upper() + neweID[2:]

        phoneMatch = re.search("\d{3}[-]\d{3}[-]\d{3}", pNum)
        while not phoneMatch:
            print(f'Phone {pNum} is invalid')
            print("Enter phone number in form 123-456-7890")
            pNum = input("Enter phone number: ")
            phoneMatch = re.search("\d{3}[-]\d{3}[-]\d{3}", pNum)


        if eID in personDict.keys():
            print("WARNING: DUPLICATE EMPLOYEE ID USED")

        p = Person(fName, lName, mid, eID, pNum) #Create Person object
        personDict[p.employeeID] = p # Key is EmployeeID, mapped to Person object
    return personDict


def file_method():

    if len(sys.argv) > 1:
        arg_input = sys.argv[1]
        with open(os.path.join(os.getcwd(), arg_input), 'r') as f:
            text_in = f.read()
        return text_in
    else:
        print("Did not enter path name ")
        exit(-1) #User did not specify sysarg. End the program


if __name__ == '__main__':
    text_in = file_method() #fetch and check open file, returns text from data file
    personDict = process_txt(text_in)  #Dict returned after processing each person
    #save pickle file
    pickle.dump(personDict, open('dict.p', 'wb'))
    print("\nEmployee list: \n")
    #read the pickle file
    dict_in = pickle.load(open('dict.p', 'rb'))
    #display each Person Object
    for key in dict_in:
        dict_in[key].display()
        print("\n")




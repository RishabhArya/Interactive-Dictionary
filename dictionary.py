import json
from fuzzywuzzy import fuzz
#from fuzzywuzzy import process

datastore = json.load(open("data.json", "r"))
word = input("Enter the word to be searched:- ")
word = word.lower()
'''if word in datastore.keys():
    print(word, "-", "\n", datastore[word])
else:
    print("No meaning found")'''
for key in datastore:
    ratio = fuzz.partial_ratio(word, key)
    if (ratio == 100):




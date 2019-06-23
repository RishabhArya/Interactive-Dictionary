import json
import difflib
datastore = json.load(open("data.json", "r"))
word = input("Enter the word to be searched:- ")
word = word.lower()
if word in datastore.keys():
    print(word, "-", "\n", datastore[word])
else:
    possibilities = difflib.get_close_matches(word, datastore, n=3, cutoff=0.6)
    print("Do you mean")
    num = 1
    for key in possibilities:
        print(num,key)
        num = num + 1
    print("4 No One")
    opt = input()
    opt = int(opt)
    if opt == 4:
        print("No meaning found")
    else:
        opt = opt - 1
        word = possibilities[opt]
        print(word, "-", "\n", datastore[word])
# script to tokenize text
# 1) create a .txt file of all comments
# 2) replace the name of the file and change the output file name

import string

# open the file in read mode
text = open("reasons.txt","r")

# create an empty dictionary
d = dict()

# loop through each line of the file
for line in text:
  # remove the leading spaces and newline character
  line=line.strip()
  # convert the characters in line to lowercase to avoid mismatch
  line=line.lower()
  # remove the pounctuation marks from line
  line=line.translate(line.maketrans("","",string.punctuation))
  # split the line into words
  words=line.split(" ")
  # iterate over each word in line
  for word in words:
    # check if the word is already in the dictionary
    if word in d:
        # increment count of word by 1
        d[word] = d[word]+1
        else:
          # add the word to dictionary with count 1
          d[word] = 1
    # print the contents of dictionary
    with open("reasons.csv", "w") as f:
      for key in list(d.keys()):
        f. write("%s,%s\n"%(key,d[key]))
        print(key,":",d[key])

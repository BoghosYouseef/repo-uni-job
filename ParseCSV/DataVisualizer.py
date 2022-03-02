import pandas as pd
import re

#df = pd.read_csv("20220112_power2.csv", sep=";",encoding="latin1")#, on_bad_lines='skip') 
FILE_LINES = []

with open("20220112_power2.csv", encoding="latin1") as data:
   #print(data.readlines())
    #FILE_LINES = data.readlines()
    head = [next(data) for line in range(20)]

for i in range(len(head)):
    print(f"{i} ------ {head[i] }")



def testing_code_generated_online(regex, test_str):
    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        if match.group() != (";" or "" or " "):

            print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

#        for groupNum in range(0, len(match.groups())):
#            groupNum = groupNum + 1
#            
#            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))



pattern = "(\w|\s|\d|\.|:|,)*(;|$)"
testing_code_generated_online(pattern, head[4])
testing_code_generated_online(pattern, head[5])
if __name__ == "__main__":
    pass

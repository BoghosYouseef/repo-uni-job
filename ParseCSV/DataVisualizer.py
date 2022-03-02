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
        
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))



testing_code_generated_online("(\w|\s|\d|\.|:|,)*(;|$)", head[5]):
#pattern = ";?((\s)*|(\d)*|(\w*)|(,)*|(\.)*|(:)*)*;"

print("number of fields = ",len(re.findall(pattern, head[5])))
print("the fields are:", re.findall(pattern, head[5]))
print("number of fields for categories = ",len(re.findall(pattern, head[4])))
print("the fields are:", re.findall(pattern, head[4]))
if __name__ == "__main__":
##   print(pd.__version__) 
#
#    print("first 10 lines of the file")
#    print("-"*20)
#    print(df.head(10))
#    print("-"*20)
#    print("last 10 lines of the file")
#    print(df.tail(10))
#    print("-"*20)
#    print("showing full df")
#    print(df)
    pass

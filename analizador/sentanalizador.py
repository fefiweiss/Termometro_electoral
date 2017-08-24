import json

# load data
with open("sentiment.json", "r") as jsonfile:
    data = json.load(jsonfile)

average = []
s = [0,0,0,0] # neg, pos, neu and compound


for candidate in data:
    print candidate
    for score in data[candidate]:
        s[0] += score["neg"]
        s[1] += score["pos"]
        s[2] += score["neu"]
        s[3] += score["compound"]
    finalscore = [score/len(data[candidate]) for score in s]
    finalscore.append(candidate)
    average.append(finalscore)
    s = [0,0,0,0]

print average

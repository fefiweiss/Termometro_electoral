import csv
import json

docs = ["carolinagoic.csv", "eduardo_artes.csv", "guillier.csv", "joseantoniokast.csv", "labeasanchez.csv", "marcoporchile.csv", "sebastianpinera.csv", "senadornavarro.csv"]
corpus = []

for doc in docs:
    candidate = []
    with open("traducidos/"+doc,"r") as csvfile:
        header = csvfile.readline()
        freader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in freader:
            candidate.append(row)
    corpus.append(candidate)

# sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#print corpus


overall = []
sid = SentimentIntensityAnalyzer()
for candidate in corpus:
    polarity = []
    #print candidate
    for tweet in candidate:
        print tweet
        print "fin"
        if tweet:
            polarity.append(sid.polarity_scores(tweet[0].strip()))
    overall.append(polarity)

# save
data = {}
for i,name in enumerate(docs):
    data[name] = overall[i]
    
with open('sentiment.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
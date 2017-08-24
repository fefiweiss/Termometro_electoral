# -*- coding: utf-8 -*-
import json
import csv
from googletrans import Translator

def translate_csv2(candidate):
    """ translate a given dataset """
    translator = Translator()
    tweets = []

    print(candidate)
    with open('tweets/'+candidate+'_tweets.csv', 'r') as file:
        header = file.readline()
        ttread = csv.reader(file, delimiter=',', quotechar='"')
        for i, row in enumerate(ttread):
            try:
                row[2]= translator.translate(row[2].decode('utf-8'), src='es', dest='en').text.encode('utf-8')
                tweets.append(row[2])
            except ValueError:
                print("document %d was not translated" % i)

    with open('traducidos/'+candidate+'.csv','w') as output:
        output.write('profile,'+header)
        for entry in tweets:
            output.write('"'+entry+'"\n')


def main():
    #candidates = ['marcoporchile', 'sebastianpinera','senadornavarro']
    candidates = ["sebastianpinera","carolinagoic","eduardo_artes","guillier","joseantoniokast", "marcoporchile","senadornavarro","labeasanchez"]
    for candidate in candidates:
        translate_csv2(candidate)

    # filename and attribute to translate are required
    #if args.filename and args.attr:
    #    start = time.time()
    #    translate_json(args.filename, args.attr, args.outputfile)
    #
    #    print("elapsed time: %f" % (time.time()-start))
    #else:
    #   print("FILENAME and ATTRIBUTE are required. See -h or --help.")

if __name__ == '__main__':
    main()

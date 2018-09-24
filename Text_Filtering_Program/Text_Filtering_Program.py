#Perren Wright, Peoplesoft ID: 1390436
#Program #3: Detecting Trends and Foul Language in Twitter
#COSC 1306, Fall 2017
#This program detects trends and foul language in text files

#This part of the code adds curse words to my file
with open('swear_words.txt','a+') as f:
    f.write('bitch')
    f.write('\n'+ 'motherfucker')
#This part of the code will find the offensive tweets and print them to a new file
def cursionary(filename):
    badwords = ['fuck', 'shit', 'cunt', 'bitch', 'motherfucker', 'whore', 'asshole', 'pussy', 'dick', 'slut', 'idiot']
    lines = []
    with open(filename,'r', encoding='utf-8') as z:
        for line in z:
            for word in badwords:
                if word in line:
                    line = line.strip()
                    lines.append(line)
                    with open('potientially_offensive_tweets.txt','w') as u:
                        for line in lines:
                            u.write("%s\n" % line)
cursionary('twitter_data.txt')
#This part of the code detects trending topics on twitter
import re
from collections import Counter
def topictrends(filename,N):
    with open(filename,'r', encoding='utf-8') as k:
        for line in k:
            data = k.read()
            linez = re.findall(r"(#\w+)", data)
            g = Counter(linez).most_common(N)
            with open('top_hashtags.txt','w') as q:
                for item in g:
                    q.write("%s\n" % (str(item)))
topictrends('twitter_data.txt', 2)

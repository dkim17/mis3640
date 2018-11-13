from twython import Twython
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Replace the following strings with your own keys and secrets
TOKEN = '295995929-EF7PArCGbluVIJjVRUz3aYPwhkQA76lNkFTXlBQ3'
TOKEN_SECRET = '1hkQaoUXT8DLjmDxbyGEHE8KDxvFH1e7asIorx4OFKUch'
CONSUMER_KEY = 'mVOQriBHMwFeT6sWsj6gIl4PE'
CONSUMER_SECRET = 'hkbTzvBP32JINElkMQ2TY3Lxi8qB0X5izqW9inzI5qP8iQ41ob'

t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Sk", count=2500)
data1 = t.search(q="Doosan", count=2500)

lebron = 0
lebronpos = 0
lebronneg = 0
curry = 0
currypos = 0
curryneg = 0


for status in data['statuses']:
    score = SentimentIntensityAnalyzer().polarity_scores(status['text'])
    lebron += score['compound']
    lebronpos += score['pos']
    lebronneg += score['neg']

for status in data1['statuses']:
    score = SentimentIntensityAnalyzer().polarity_scores(status['text'])
    curry += score['compound']
    currypos += score['pos']
    curryneg += score['neg']



print ('The Compound Score for Lebron on Twitter for the most recent 2,500 twitt is {:2f}, pos: {:1f}, neg: {:01f}'.format(lebron, lebronpos, lebronneg))
print ('The Compound Score for Curry on Twitter for the most recent 2,500 twitt is {:2f}, pos: {:1f}, neg: {:01f}'.format(curry, currypos, curryneg))





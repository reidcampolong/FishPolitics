import twitter
import re
import credentials

api = twitter.Api(consumer_key=credentials.consumer_key,
                  consumer_secret=credentials.consumer_secret,
                  access_token_key=credentials.access_token_key,
                  access_token_secret=credentials.access_token_secret)

languageFilter = {
    "rebuild": "avenge",
    "witnesses": "these dudes I know",
    "allegedly": "kinda probably",
    "new study": "tumblr post",
    "rebuild": "avenge",
    "space": "spaaace",
    "russia": "Putin-ville",
    "nation": "tribe",
    "electric": "atomic",
    "election": "eating contest",
    "senator": "elf-lord",
    "sen": "elf-lord",
    "taxpayers": "peasants",
    "workers": "slaves",
    "president": "captain",
    "trump": "supreme overlord Trump",
    "gas": "energy substance",
    "investigation": "wild goose-hunt",
    "evidence": "cookie trail",
    "interview": "parley",
    "republican": "elephant worshipper",
    "rep": "elephant worshipper",
    "dem": "donkey rider",
    "democrat": "donkey rider",
    "congress": "the circus"
}

# CNNPolitics, HuffPost, nytpolitics
USERS = ['13850422', '15458694', '14434063', '9300262']
base_status_url = "https://twitter.com/$user/status/"

"""
Replace political jargon with weird words!
"""
def jargonify():
    for tweet in api.GetStreamFilter(follow=USERS, filter_level="medium"):
        jargonTweet = jargonifyTweet(tweet['text']) + " - " + getOriginalURL(tweet['user']['screen_name'], tweet['id'])
        api.PostUpdate(jargonTweet)
        print("NEW TWEET POSTED: " + jargonTweet)

"""
Turn a tweet into jargon word by word
"""
def jargonifyTweet(tweet) -> str:
    for word in tweet.split(" "):
        # If word is a link, remove it from tweet
        if word.startswith('http'):
            tweet = tweet.replace(word, '')
        else:
            filteredWord = filterWord(word).lower()
            if filteredWord in languageFilter:
                tweet = tweet.replace(word, languageFilter[filteredWord])
    return tweet

"""
Replace foreign characters inside of a word/phrase
"""
def filterWord(word) -> str:
    return re.sub('[^a-zA-Z0-9\n\n]', '', word)

"""
Get a URL to a tweet from a tweet ID and account name
"""
def getOriginalURL(user, tweetID):
    return base_status_url.replace('$user', user) + str(tweetID)

# Main method
jargonify()

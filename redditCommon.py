import praw
from collections import Counter
import nltk
from nltk.corpus import stopwords

reddit = praw.Reddit(
    client_id = 'Insert Client ID',
    client_secret = 'Insert Secret',
    user_agent = 'Word Counter by /u/Chillbyvl'
)

def determineCategory(category, subreddit, postSearchAmount):
    categoryNames = {
        'top': subreddit.top,
        'hot': subreddit.hot,
        'new': subreddit.new,
    }
    return categoryNames.get(category, lambda **kwargs: unknownCategory())(limit=postSearchAmount)

def unknownCategory():
    raise ValueError("Specify the category to be 'top', 'hot', or 'new'.")

def redditCommon(subreddit, postSearchAmount, category):
    subreddit = reddit.subreddit(subreddit)
    wordBank = []
    submissions = determineCategory(category, subreddit, postSearchAmount)
    for submission in submissions:
        words = nltk.word_tokenize(submission.title)
        stop_words = set(stopwords.words('english')) # removes common words that don't contribute useful info.
        words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
        wordBank.extend(words)
    commonWords = Counter(wordBank).most_common(10) # can modify to show top __ most common words; example = 10
    print(f"Most common words in /r/{subreddit}'s {category} category among {postSearchAmount} posts")
    for word, count in commonWords:
        print(f"{word}: {count}")

# set parameters based on desired search
subreddit = 'FireEmblemHeroes'
postSearchAmount = 50
category = 'hot'

redditCommon(subreddit, postSearchAmount, category)

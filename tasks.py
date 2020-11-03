from textblob import TextBlob
import praw


reddit = praw.Reddit('bot')

reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jkq2yu/us_spies_say_the_hunter_biden_email_controversy/' #can do multiple

submission = reddit.submission(url=reddit_debate_url)

for comment in submission.comments.list():  
    chosen_comment = TextBlob(comment.body.lower())
    polarity = chosen_comment.sentiment.polarity
    if 'biden' in comment.body.lower() and polarity < 0:
        comment.downvote()
        #print ('comment downvote')
    if 'biden' in comment.body.lower() and polarity >= 0:
        comment.upvote()
        #print ('comment upvote')
    if 'trump' in comment.body.lower() and polarity < 0:
        comment.upvote()
    if 'trump' in comment.body.lower() and polarity >= 0:
        comment.downvote()

#submission EC

g = reddit.subreddit('csci040temp')

for submission in g.new(limit=None):
    phrase = TextBlob(submission.title.lower())
    if 'biden' in submission.title.lower():
        if phrase.sentiment.polarity < 0:
            submission.downvote()
            #print ('comment downvote')
        if phrase.sentiment.polarity > 0:
            comment.upvote()
            #print ('comment upvote')
    if 'trump' in submission.title.lower():
        if phrase.sentiment.polarity < 0:
            submission.upvote()
        if phrase.sentiment.polarity > 0:
            submission.downvote()




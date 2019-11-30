import tweepy

import time




# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.


CONSUMER_KEY = 'Uigusv2sPHWZbOBV68XKo9sqL'
CONSUMER_SECRET = 'qOQyFhBcr8DKRWXzJC4DkTgJUahLPA5fIF34LQkQoVVlDtuh7N'
ACCESS_KEY = '1194200239520927744-tXmCseaydMS020eHeelkDBu4Tw8OD4'
ACCESS_SECRET = 'p3exfI6DBm6o29KaFMXezLhRsIlhBmq8mcZkuduf143Av'

print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '' in mention.full_text.lower():
            print('Got a tweet', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                   mention.full_text , mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

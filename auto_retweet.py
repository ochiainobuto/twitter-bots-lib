# -*- coding: utf-8 -*-

import time
from datetime import datetime
import twitter
import secret

api = twitter.Api(
    consumer_key = secret.twDict['consumer_key'],
    consumer_secret = secret.twDict['consumer_secret'],
    access_token_key = secret.twDict['access_token_key'],
    access_token_secret = secret.twDict['access_token_secret']
    )

def get_search(term):
    return api.GetSearch(term=term, count=100, result_type='recent')

def post_retweet(tweetid):
    try:
        api.PostRetweet(tweetid)
    except:
        print(u'既にリツイートされています') # って書いてるけど、相手にブロックされている場合もこちら

def search_and_retweet(term, rm_nonurl=False):
    for t in get_search(term):                                           
        nowtime = int(time.mktime(datetime.now().timetuple()))
        # ツイート内容及びscreen nameにbotが含まれる場合、除外する
        if u'bot' in t.text or u'bot' in t.user.screen_name:
            break
        # urlが含まれないツイートを排除する（引数で設定）
        if rm_nonurl is True and len(t.urls) == 0: 
            break
        # 1時間以内のツイートをリツイートする
        if t.created_at_in_seconds in range(nowtime-60*60, nowtime):
            post_retweet(t.id)

search_and_retweet(u'keras')
search_and_retweet(u'tensorflow', True)
search_and_retweet(u'pytorch', True)
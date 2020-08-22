# -*- coding: utf-8 -*-

import time
from datetime import datetime
import twitter
import secret

CK='a5nttkJQz8PobISloKPnxeM8E'
CS='cEzagoJYk1ZtlmVjN7CEerywVS5s57TywJDtlTg3omSYfdYNe7'
AT='1233983232305033216-FjZq4FhLshWbQC7IYGGfsxnfvSKS57'
AS='unaRXD0HgtHngMQX8HREbmJrOGjTsRquvVNaZWYWUTBzl'

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

# 1ツイートずつループ
def search_and_retweet(term):
    for status in api.search(q=term, lang='ja', result_type='recent',count=12):
        tweet_id = status.id
        # 例外処理をする
        try:
            # リツイート実行
            api.retweet(tweet_id)
        except:
            print('error')
    
search_and_retweet(u'keras')
search_and_retweet(u'tensorflow')
search_and_retweet(u'pytorch')    

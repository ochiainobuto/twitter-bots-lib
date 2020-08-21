# -*- coding: utf-8 -*-

import time
from datetime import datetime
import twitter
import secret

CK = 'owmfVDnAGuHYaTLiO59cyxLhY'
CS = 'RvZzePeciSmSFQbkQyxuNy8N0YWURKAG2ldgd0lW0FhVWssE52'
AT = '1254252741502709765-YSQKdjttlT37suWU3AgkdEGS2NNyEb'
AS = 'FqIMD94c7BjCcc08WNlAgJ3gXIEePUedM3G4tQYkzTARx'

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

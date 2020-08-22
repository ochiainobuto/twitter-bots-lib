# -*- coding:utf-8 -*-
import tweepy
import emoji
from janome.tokenizer import Tokenizer
import collections
import random

word_list = [
    'keras', 'tensorflow', 'pytorch', '機械学習', '深層学習', 'AI', 'Unet', '物体検出', 'セグメンテーション'
]

serch_word = random.choice(word_list)


def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)


tweet_list = []
emojis = ' 🤗⭕🤓🤔🤘🦁⭐🆗🆖🈲🤐🤗🤖🤑🆙⏩'

CK='a5nttkJQz8PobISloKPnxeM8E'
CS='cEzagoJYk1ZtlmVjN7CEerywVS5s57TywJDtlTg3omSYfdYNe7'
AT='1233983232305033216-FjZq4FhLshWbQC7IYGGfsxnfvSKS57'
AS='unaRXD0HgtHngMQX8HREbmJrOGjTsRquvVNaZWYWUTBzl'

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

tweet_data = api.search(q=serch_word, count=100)

for tweet in tweet_data:
    #     print(tweet.text)
    tweet_text = tweet.text.replace('\n', '')
    tweet_text = tweet_text.replace('\u3000', '')
    tweet_text = tweet_text.replace('\u200d️', '')
    tweet_text = tweet_text.replace('＼', '')
    tweet_text = tweet_text.replace('https', '')

    tweet_text = remove_emoji(tweet_text)

    tweet_split = tweet_text.split(':')

    if len(tweet_split) > 1:
        tweet_list.append(tweet_split[1])
    else:
        tweet_list.append(tweet_text)

    remove_list = []
    for line in tweet_list:
        #         print(line)
        if len(line) > 0:
            if line[0] == '＃':
                remove_list.append(line)
            if line[0] == '@':
                remove_list.append(line)
            if line[0] == '/' and line[1] == '/':
                remove_list.append(line)
            if line[0] == 'R' and line[1] == 'T':
                remove_list.append(line)

    for line in remove_list:
        tweet_list.remove(line)

next_max_id = tweet_data[-1].id
for i in range(2, 110):
    try:
        tweet_data = api.search(q=serch_word,
                                count=100,
                                max_id=next_max_id - 1)
        next_max_id = tweet_data[-1].id
        for tweet in tweet_data:
            tweet_text = tweet.text.replace('\n', '')
            tweet_text = tweet_text.replace('\u3000', '')
            tweet_text = tweet_text.replace('\u200d️', '')
            tweet_text = tweet_text.replace('＼', '')
            tweet_text = tweet_text.replace('https', '')

            tweet_text = remove_emoji(tweet_text)

            tweet_split = tweet_text.split(':')

            if len(tweet_split) > 1:
                tweet_list.append(tweet_split[1])
            else:
                tweet_list.append(tweet_text)

            remove_list = []
            for line in tweet_list:
                #         print(line)
                if len(line) > 0:
                    if line[0] == '＃':
                        remove_list.append(line)
                    if line[0] == '@':
                        remove_list.append(line)
                    if line[0] == '/' and line[1] == '/':
                        remove_list.append(line)
                    if line[0] == 'R' and line[1] == 'T':
                        remove_list.append(line)

            for line in remove_list:
                tweet_list.remove(line)
    except:
        pass

##### 名詞を抜き出す #####
tokenizer = Tokenizer()
noun_list = []

for sentence in tweet_list:
    for token in tokenizer.tokenize(sentence):
        word = str(token).split('\t')
        if word[1].split(',')[0] == "名詞" and word[1].split(',')[1] == "一般":
            noun_list.append(word[0])

c = collections.Counter(noun_list)
_c = c.most_common()

tweet_word = 'Twitterで「' + serch_word + '」を検索したときに多く含まれる名詞ベスト１０---'
for i in range(1, 11):
    tweet_word = tweet_word + '■' + str(i) + '位: ' + str(_c[i][0]) + ':' + str(
        _c[i][1]) + '回 '

api.update_status(tweet_word)

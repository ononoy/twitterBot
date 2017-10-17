import requests
from requests_oauthlib import OAuth1Session

#取得したkeyを以下で定義する
access_token = ''
access_token_secret = ''
consumer_key = 'MnUX1YXrP0HKDKmnLoFaJ5TJl'
consumer_key_secret = 'uNVJspPhSXahCJddgzPyWYj1NGau4MukSsSG2maaeLNyPyLy8h'

#Consumer Key (API Key)MnUX1YXrP0HKDKmnLoFaJ5TJl
#Consumer Secret (API Secret)uNVJspPhSXahCJddgzPyWYj1NGau4MukSsSG2maaeLNyPyLy8h
#Access LevelRead and write (modify app permissions)
#Owneronono_room
#Owner ID2481425874



# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#パラメータの定義
params = {'screen_name':'AbeShinzo',
          'exclude_replies':True,
          'include_rts':False,
          'count':200}
#'screen_name':ユーザーを指定。twitterアカウントの@以降を入力だよ〜〜〜〜！
#'exclude_replies':リプライを含むかどうか
#'include_rts':リツイートを含むかどうか
#'count':一度に取得するツイート件数の指定。デフォルト20、maxで200。




#APIの認証
twitter = OAuth1Session(consumer_key, consumer_key_secret, access_token, access_token_secret)

#リクエストを投げる
res = twitter.get(url, params = params)
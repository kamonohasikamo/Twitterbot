import tweepy

#TwitterAPI Key
CK = ""
CS = ""
AT = ""
AS = ""

#Create TwitterObject
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

#実際にツイートしてみる
api.update_status("Pythonから自動ツイートしてみる")

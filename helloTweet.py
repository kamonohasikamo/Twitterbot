#-*- coding: utf-8 -*-
import tweepy
import io, sys, urllib3
import random

#TwitterAPI Key
CK = ""
CS = ""
AT = ""
AS = ""

#Create TwitterObject
# auth = tweepy.OAuthHandler(CK, CS)
# auth.set_access_token(AT, AS)
#
# api = tweepy.API(auth)

#Auto Tweet
#api.update_status("Pythonから自動ツイートしてみる")
#1ツイートずつループ
# for status in api.user_timeline(id=''):
# 	#見映えのため区切る
# 	print('-------------------------------------------')
# 	#ユーザ名表示
# 	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys.stdout.encoding, errors="ignore")
# 	print('name:' + status.user.name)
# 	#内容表示
# 	print(status.text)

text_list = ["今日の運勢は　パンナコッタ","今日の運勢は　大凶　です（＾＾＾）", "今日の運勢、的に凶な気がするのでそういうことで!","今日の運勢は　しょうがないから吉で","今日の運勢は明日教えます","今日の運勢は　たぶんすごいよ", "今日の運勢は　最凶　です！残念", "占うのめんどくなってきた", "今日の運勢は　君の心の中に答えはある――――　"]  # ここに返信する文字列をいくつか入れて置く
#
# class Listener(tweepy.StreamListener):
#
# 	# ツイートを取得
# 	def on_status(self, status):
# 		# リツイートや引用リツイートは除外する
# 		if (not status.retweeted) and ("RT @" not in status.text):
# 			# "おみくじ"という文字列がツイートに含まれていた場合
# 			if "おみくじ" in status.text:
# 				# ツイートを用意
# 				tweet = "@" + str(status.user.screen_name) + "\n" + random.choice(text_list)
#
# 				# ツイートする
# 				api.update_status(tweet, status.id)
#
# 				# 確認のためターミナルに出力
# 				sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys.stdout.encoding, errors="ignore")
# 				print(status.user.name + "\n" + status.text)
# 				print("-> " + tweet)
# 				print("----------------")
#
# 				return True
#
# 	# エラー時の処理
# 	def on_error(self, status_code):
# 		print('Got an error with status code: ' + str(status_code))
# 		return True
#
# 	# タイムアウトした時の処理。サーバーなどで動かす時は必要。
# 	def on_timeout(self):
# 		print('Timeout...')
# 		return True
#
# listener = Listener()
# stream = tweepy.Stream(auth, listener, secure=True)
# stream.userstream()

# class Listener(tweepy.StreamListener):
# 	def on_status(self, status):
# 		status.created_at += datetime.timedelta(hours=9)
#
# 		# リプライが来たら返信
# 		if api.user_timeline(id=''):
# 			tweet = "@" + str(status.user.screen_name) + " " + "Hello！\n" + str(datetime.datetime.today())
# 			api.update_status(status=tweet)
# 			return True
#
# 	def on_error(self, status_code):
# 		print('Got an error with status code: ' + str(status_code))
# 		return True
#
# 	def on_timeout(self):
# 		print('Timeout...')
# 		return True
#
# # Twitterオブジェクトの生成
# auth = tweepy.OAuthHandler(CK, CS)
# auth.set_access_token(AT, AS)
#
# listener = Listener()
# stream = tweepy.Stream(auth, listener)
# stream.userstream()

#スクリプトファイルとして実行されると
if __name__ == '__main__':

	#例外処理
	try:

		#authにCONSUMER_KEYとCONSUMER_SECRETを渡す
		auth = tweepy.OAuthHandler(CK, CS)

		#authにアクセストークンをセットする
		auth.set_access_token(AT, AS)

		#記述を楽にする
		api = tweepy.API(auth)

		#タイムラインから10投稿取得するまでループする
		for status in api.home_timeline(count=15)[::-1]:

			#見やすくするための線
			print('-----------------------------------------------------')

			#ユーザーネームを出力
			print('name:' + status.user.name)
			print('userID:' + status.user.screen_name)

			#投稿内容を出力
			print(status.text)
			if (not status.retweeted) and ("RT @" not in status.text):
				# "おみくじ"という文字列がツイートに含まれていた場合
				if "" in status.text:
					# ツイートを用意
					tweet = "@" + str(status.user.screen_name) + "\n" + random.choice(text_list)

					# ツイートする
					api.update_status(tweet, status.id)


	#エラーが発生した場合TweepErrorが返ってくる
	except tweepy.TweepError as e:
		#エラー内容を出力
		print(e.reason)

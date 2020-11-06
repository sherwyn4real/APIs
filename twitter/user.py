import tweepy
import os

def getUser(username):
    print(os.environ['API_KEY'])
    auth = tweepy.OAuthHandler(os.environ['API_KEY'],os.environ['API_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'],os.environ['ACCESS_SECRET'])
    api = tweepy.API(auth)

    try:
        user = api.get_user(username)
        user_timeline = tweepy.Cursor(api.user_timeline,username)
    except:
        error_dict = {"status": 404,"message": "tweets not found"}
        return error_dict,404

    user_data = {}
    user_data['user_name'] = user.name
    user_data['user_screen_name'] = user.screen_name
    user_data['followers_count'] = user.followers_count
    user_data['friends_count'] = user.friends_count
    user_data['tweets'] = []

    for status in user_timeline.items(10):
        user_data['tweets'].append({'created_at': str(status.created_at),'text':status.text})

    return user_data,200

import requests

def get_random_post():
    return requests.get(
        'https://reddit.com/r/rarepuppers/random.json',
        headers = {'User-agent': 'wow soy un perrito'}
    ).json()[0]['data']['children'][0]['data']

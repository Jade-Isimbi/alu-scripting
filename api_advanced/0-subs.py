import requests

""" returns the number of subscribers """

def sub_counter(sub_reddit):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    URL = f"https://api.reddit.com/r/{sub_reddit}/about"

    response = requests.get(URL, allow_redirects=False, headers={'User-Agent': USER_AGENT}).json()
    subscriber_count = response['data']['subscribers']

    print(subscriber_count)

sub_counter('liminalspace')


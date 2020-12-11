import requests


def key_Word():
    response = requests.get(keyword_url)
    return response.json()["data"]


if __name__ == '__main__':
    for kw in key_Word():
        print(kw)

import requests
from automated.settings import proxy_url


def get_random_proxy():
    """
    get random proxy from proxyPool
    :return: proxy
    """
    return requests.get(proxy_url).text.strip()


if __name__ == '__main__':
    for _ in range(100):
        print(get_random_proxy())

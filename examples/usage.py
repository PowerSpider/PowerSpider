# from powerspider.Download import downloader
#
# if __name__ == '__main__':
#     # print(downloader("https://www.baidu.com/", "GET"))
#     downloader("https://www.baidu.com/", "GET")

import requests
import cchardet

#
# print("response.status_code:", response.status_code)
# print("response.headers:", response.headers)
# print("response.request.headers:", response.request.headers)
# print("response.content:", response.content)
# print("response.text", response.text)

urls = 'http://httpbin.org/get'
from powerspider.tools.Ua import ua


def downloader(url, method=None, header=None, binary=False):
    _headers = header if header else {'User-Agent': ua()}
    _method = "GET" if not method else method
    response = requests.request(url, method=_method, headers=_headers)
    encoding = cchardet.detect(response.content)['encoding']
    return response.content if binary else response.content.decode(encoding)


print(downloader(urls, method="POST"))

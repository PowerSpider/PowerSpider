from powerspider.Download import downloader

if __name__ == '__main__':
    # print(downloader("https://www.baidu.com/", "GET"))
    response = downloader("https://www.baidu.com/", "GET")
    print("response.status_code:", response.status_code)
    print("response.headers:", response.headers)
    print("response.request.headers:", response.request.headers)
    print("response.content:", response.content)
    print("response.text", response.text)

import cchardet
from retrying import retry
from toolSet.Ua import ua
from loguru import logger
from requests import request, RequestException


class BasicSpider:

    @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=2000)
    def downloader(self, url, method=None, header=None, timeout=None, binary=False, **kwargs):
        logger.info(f'Scraping {url}')
        # 默认超时
        _maxTimeout = timeout if timeout else 5
        # 自定义Ua
        _headers = header if header else {'User-Agent': ua()}
        # 默认请求方法
        _method = "GET" if not method else method
        try:
            response = request(method=_method, url=url, headers=_headers, **kwargs)
            encoding = cchardet.detect(response.content)['encoding']
            if response.status_code == 200:
                return response.content if binary else response.content.decode(encoding)
            elif 200 < response.status_code < 400:
                logger.info(f"Redirect_URL: {response.url}")
            logger.error('Get invalid status code %s while scraping %s', response.status_code, url)
        except RequestException as e:
            logger.error(f'Error occurred while scraping {url}, Msg: {e}', exc_info=True)

    def download(self):
        pass


if __name__ == '__main__':
    basic = BasicSpider()
    print(basic.downloader("http://www.baidu.com/"))

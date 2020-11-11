from powerspider.Download import downloader
from powerspider.tools import ConversionDictionary
import requests

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'shopping-bag-migration=shopperId=&isMigrated=true; Bd34bsY56=AGZwz7J1AQAAmBaPYb7w3EPiz-b1zdNELFpD-E-uyi_MpmcylXbGVpwRvEmB; Ad34bsY56=AAVsz7J1AQAA64IPYO9BO8YV_0wCGgTRiC63IYjBynAt3Tb_XWDmNl93p684|1|1|cebff3eedc779034393fcc9abbde7cfbaef94940',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://www.nordstrom.com/s/5588826',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
}
response = requests.get(url=urls, headers=header)
print(response.text)
with open("5588826.html", "a+", encoding="utf-8") as f:
    f.write(response.text)
# print(
#     downloader("https://www.nordstrom.com/s/chelsea28-turtleneck-sweater"
#                "/4030029?origin=category-personalizedsort&breadcrumb=Home%2FBrands%2FNordstrom%20"
#                "Made%2FWomen&color=tan%20dale", header=header)
# )

import requests
from bs4 import BeautifulSoup

url = 'https://www.data.jma.go.jp/stats/etrn/view/daily_a1.php?prec_no=44&block_no=1001&year=2024&month=3&day=15&view='
response = requests.get(url)
response.encoding = response.apparent_encoding 

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(response.text, 'html.parser')

# <tr>タグの文字列を取得する
# <tr class="mtx" style="text-align:right;">
rows = soup.find_all('tr', {'class': 'mtx', 'style': 'text-align:right;'})


# 指定の日付
target_day = '15'

# title タグの文字列を取得する
target_row = soup.find('a', string=target_day).find_parent('tr')

if target_row:
    values = [td.text.strip() for td in target_row.find_all('td')]

    result = f"{values[0]}日, {values[1]}mm, {values[4]}℃, {values[5]}℃, {values[6]}℃"

    print(result)

    #     # テキストファイルに保存する
    # with open('WeatherHistorySearchSoup.html', 'w', encoding='utf-8') as file:
    #     file.write(str(result))
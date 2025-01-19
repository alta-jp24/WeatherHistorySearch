import requests

url = 'https://www.data.jma.go.jp/stats/etrn/view/daily_a1.php?prec_no=44&block_no=1001&year=2024&month=3&day=15&view='
response = requests.get(url)
response.encoding = response.apparent_encoding 

# HTMLファイルに保存する
with open('WeatherHistorySearch.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
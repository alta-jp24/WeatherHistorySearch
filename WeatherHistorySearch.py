import requests
from bs4 import BeautifulSoup

# 日付指定定義
dates = [
    {'year': 2024, 'month': 3, 'day': 15},
    {'year': 2023, 'month': 3, 'day': 15},
]

# 場所定義
prec_no = 44
block_no = 1001


results = ["日付,降水量,平均気温,最高気温,最低気温\n"]

for date in dates:
    # urlの設定
    url = f"https://www.data.jma.go.jp/stats/etrn/view/daily_a1.php?prec_no={prec_no}&block_no={block_no}&year={date['year']}&month={date['month']}&day={date['day']}&view="

    response = requests.get(url)
    response.encoding = response.apparent_encoding 

    # BeautifulSoup オブジェクトを作る
    soup = BeautifulSoup(response.text, 'html.parser')

    target_row = soup.find('a', string=date['day'])
    target_row = target_row.find_parent('tr') if target_row else None

    if target_row:
        values = [td.text.strip() for td in target_row.find_all('td')]

        result = f"{date['year']}/{date['month']}/{date['day']}: {values[1]}mm, {values[4]}℃, {values[5]}℃, {values[6]}℃\n"
        results.append(result)

# テキストファイルに保存
with open('WeatherHistorySearch.txt', 'w', encoding='utf-8') as file:
    file.writelines(results)

# 出力
print("".join(results))
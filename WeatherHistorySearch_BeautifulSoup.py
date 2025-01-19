from bs4 import BeautifulSoup

# HTMLデータの読み込み
html_file = 'WeatherHistorySearch.html'
with open(html_file, 'r', encoding='utf-8') as file:
    html_data = file.read()

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(html_data, 'html.parser')

# 指定の日付
target_day = '15'

# title タグの文字列を取得する
target_row = soup.find('a', string=target_day).find_parent('tr')

if target_row:
    values = [td.text.strip() for td in target_row.find_all('td')]

    result = f"{values[0]}日, {values[1]}mm, {values[4]}℃, {values[5]}℃, {values[6]}℃"

    print(result)

        # テキストファイルに保存する
    with open('WeatherHistorySearchSoup.txt', 'w', encoding='utf-8') as file:
        file.write(str(result))
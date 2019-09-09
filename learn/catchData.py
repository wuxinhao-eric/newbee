import requests
from bs4 import BeautifulSoup

url = 'https://nba.hupu.com/stats/players'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

info = []
link = []
for i in soup.select('.left a'):
    info.append(i.text)
    link.append(i['href'])

import pandas as pd
players = {'球员':info,'链接':link}
df = pd.DataFrame(players)
df.to_excel('D:\\player_links.xls')
info = []
for i in soup.select('tbody tr'):
    info.append(i.text.strip())

data = [{}]
for i in range(1,51):
    a, b, c, d, e, f, g, h, i, j, k, l = info[i].split('\n')
    data.append({'排名':a,'球员':b,'球队':c,'得分':d,'命中-出手':e,'命中率':f,'命中-三分':g,'三分命中率':h,'命中-罚球':i,'罚球命中率':j,'场次':k,'上场时间':l})
import pandas as pd
df = pd.DataFrame(data)
df = df[['排名','球员','球队','得分','命中-出手','命中率','命中-三分','三分命中率','命中-罚球','罚球命中率','场次','上场时间']]
df.dropna(inplace=True)
df.to_excel('D:\\players.xls')
import requests
import json
from contextlib import closing
import pandas as pd
import os
import copy
import types
from urllib.request import urlopen
import time
import random

# url = 'https://store.steampowered.com/appreviewhistogram/730?l=english&review_score_preference=0'

pre_url = 'https://store.steampowered.com/appreviewhistogram/'
lat_url = '?l=english&review_score_preference=0'

_666_games_path = '/Users/charles/PycharmProjects/Scrap_Score/venv/666_games/1.csv'

_666_games_df = pd.read_csv(_666_games_path)

now_ID = 0
nnn = 0

for index, row in _666_games_df[['QueryID']].iterrows():
    # print(row['QueryID'])
    if now_ID != row['QueryID']:
        now_ID = row['QueryID']
        url = pre_url + str(now_ID) + lat_url
        print(url)
        try:
            data = urlopen(url).read()
            bs = str(data, encoding="utf8")
            output_path = '/Users/charles/PycharmProjects/Scrap_Score/venv/666_games_json/' + str(now_ID) + '.json'
            file = open(output_path, "w")
            file.write(bs)
            file.close()

        except Exception as e:
            print(e)
        nnn+=1
        if nnn>=50:
            time.sleep(50)
            nnn=0

# try:
#     data = urlopen(url).read()
#     print(data)
#     bs = str(data, encoding="utf8")
#     print(bs)
#     file = open("test.json", "w")
#     file.write(bs)
#     file.close()
#
# except Exception as e:
#     print(e)

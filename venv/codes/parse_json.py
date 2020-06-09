import json
import time
import pandas as pd

_666_games_path = '/Users/charles/PycharmProjects/Scrap_Score/venv/666_games/1.csv'
_666_games_df = pd.read_csv(_666_games_path)

time_list = ['2017-04-01 08:00:00', '2017-05-01 08:00:00', '2017-06-01 08:00:00', '2017-07-01 08:00:00',
             '2017-08-01 08:00:00', '2017-09-01 08:00:00']

t1_stamp = int(time.mktime(time.strptime(time_list[0], "%Y-%m-%d %H:%M:%S")))
t2_stamp = int(time.mktime(time.strptime(time_list[1], "%Y-%m-%d %H:%M:%S")))
t3_stamp = int(time.mktime(time.strptime(time_list[2], "%Y-%m-%d %H:%M:%S")))
t4_stamp = int(time.mktime(time.strptime(time_list[3], "%Y-%m-%d %H:%M:%S")))
t5_stamp = int(time.mktime(time.strptime(time_list[4], "%Y-%m-%d %H:%M:%S")))
t6_stamp = int(time.mktime(time.strptime(time_list[5], "%Y-%m-%d %H:%M:%S")))

id_p_n = pd.DataFrame(columns=['ID', 'positive_count', 'negative_count'])

print(t1_stamp)
print(t2_stamp)
print(t3_stamp)
print(t4_stamp)
print(t5_stamp)
print(t6_stamp)

now_ID = 0

for index, row in _666_games_df[['QueryID']].iterrows():
    # print(row['QueryID'])

    if now_ID != row['QueryID']:
        now_ID = row['QueryID']

        filename = '/Users/charles/PycharmProjects/Scrap_Score/venv/666_games_json/' + str(now_ID) + '.json'
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        slot_list = data['results']['rollups']

        print(slot_list)

        _ski = 0
        is_start = False

        for _tt in slot_list:
            if _ski >= 6:
                break

            if _tt['date'] == t1_stamp:
                is_start = True

            if is_start:
                # print('t_stamp: ' + str(_tt['date']))
                # print('t_recom_up: ' + str(_tt['recommendations_up']))
                # print('t_recom_down: ' + str(_tt['recommendations_down']))
                id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(_tt['recommendations_up']),
                                        'negative_count': str(_tt['recommendations_down'])}, ignore_index=True)
                _ski += 1
        break
id_p_n.to_excel('p_n_stamp.xls')

# if _tt['date']==t1_stamp:
#     print('t1_stamp: '+str(_tt['date']))
#
# if _tt['date']==t2_stamp:
#     print('t2_stamp: '+str(_tt['date']))
#
# if _tt['date']==t3_stamp:
#     print('t3_stamp: '+str(_tt['date']))
#
# if _tt['date']==t4_stamp:
#     print('t4_stamp: '+str(_tt['date']))
#
# if _tt['date']==t5_stamp:
#     print('t5_stamp: '+str(_tt['date']))
#
# if _tt['date']==t6_stamp:
#     print('t6_stamp: '+str(_tt['date']))

# print(data['results']['start_date'])
# print(data['results']['end_date'])
#
# start_Time = time.localtime(data['results']['start_date'])
# st_Time = time.strftime("%Y-%m-%d %H:%M:%S", start_Time)
# print(st_Time)
#
# end_Time = time.localtime(data['results']['end_date'])
# ed_Time = time.strftime("%Y-%m-%d %H:%M:%S", end_Time)
# print(ed_Time)

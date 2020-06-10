import pandas as pd
import os

# m_u_score_xls_path='/Users/charles/PycharmProjects/Scrap_Score/venv/codes/meta_user_score.xls'
# m_u_score_df=pd.read_excel(m_u_score_xls_path)
#
# m_u_score_df['num_ratings'] = m_u_score_df['num_ratings'].str.split(' ', 1).str[0]
#
# print(m_u_score_df.info())
#
# m_u_score_df = m_u_score_df.convert_objects(convert_numeric=True)
# print(m_u_score_df.info())
#
# m_u_score_df.to_excel('meta_user_score_01.xls')

# game_score_path = '/Users/charles/PycharmProjects/Scrap_Score/venv/666_games_scores/'
# game_score_list = os.listdir(game_score_path)
# id_results = pd.DataFrame(
#     columns=['ID', 'meta_score', 'num_critic_reviews', 'user_score', 'num_ratings', 'critic_positive', 'critic_mixed',
#              'critic_negative', 'user_positive', 'user_mixed', 'user_negative'])
#
# for i in range(len(game_score_list)):
#     score_df = pd.read_excel(game_score_path + game_score_list[i], index_col=0)
#     id_results=id_results.append(score_df, ignore_index=True)
#
# id_results.to_excel('meta_user_score.xls')

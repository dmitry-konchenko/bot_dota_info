from data import db_session
from data.wards import Wards

db_session.global_init("db/wards.db")
db_sess = db_session.create_session()
wards = Wards(
    name_of_map_piece='safe_forest',
    side='dire',
    folder_path=r'wards\dire\safe_forest',

)
wards_1 = Wards(
    name_of_map_piece='hard_forest',
    side='dire',
    folder_path=r'wards\dire\hard_forest',

)
wards_2 = Wards(
    name_of_map_piece='safe_forest',
    side='radiant',
    folder_path=r'wards\dire\safe_forest',

)
wards_3 =Wards(
    name_of_map_piece='hard_forest',
    side='radiant',
    folder_path=r'wards\dire\hard_forest',

)
db_sess.add(wards)
db_sess.add(wards_1)
db_sess.add(wards_2)
db_sess.add(wards_3)
db_sess.commit()

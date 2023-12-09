from models.Statistics import Statistics
from store.pdb import PDB

db = PDB()

sql_select_statistics = '''
SELECT COUNT(*)                                AS all_count,
       COUNT(CASE WHEN type_mk = 1 THEN 1 END) AS count_mk_1,
       COUNT(CASE WHEN type_mk = 2 THEN 1 END) AS count_mk_2
FROM user_data.customers;
'''


def select_statistics():
    data = db.execute_fetchone(sql_select_statistics)
    return Statistics(*data)

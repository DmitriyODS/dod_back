from store.pdb import PDB
from models.Customer import Customer

db = PDB()

sql_select_customers = '''
SELECT id,
       fio,
       email,
       city,
       school,
       class_school,
       type_mk,
       is_finished
FROM user_data.customers
WHERE is_finished = %s
  AND fio LIKE %s;
'''

sql_select_all = '''
SELECT count(*) as count
FROM user_data.customers;
'''

sql_select_customer = '''
SELECT id,
       fio,
       email,
       city,
       school,
       class_school,
       type_mk,
       is_finished
FROM user_data.customers
WHERE id = %s;
'''

sql_update_customer = '''
UPDATE user_data.customers
SET is_finished = true
WHERE id = %s
RETURNING id;
'''

sql_insert_customer = '''
INSERT INTO user_data.customers (fio, email, city, school, class_school, type_mk)
VALUES (%s, %s, %s, %s, %s, %s)
RETURNING id;
'''


def select_customers(filter_fio=None, is_finished=False):
    req_filter = '%%'
    req_finished = 'false'
    if filter_fio:
        req_filter = f'%{filter_fio}%'

    if is_finished:
        req_finished = 'true'

    data = db.execute_fetchall(sql_select_customers, (req_finished, req_filter))
    res = []
    for it in data:
        res.append(Customer(*it))

    return res


def select_all():
    data = db.execute_fetchone(sql_select_all)
    return data[0]


def insert_customer(customer: Customer):
    customer_id = db.execute_fetchone(sql_insert_customer, customer.placeholder_add())
    return customer_id


def select_customer_by_id(customer_id: int):
    data = db.execute_fetchall(sql_select_customer, (customer_id,))
    return Customer(*data)


def update_customer_by_id(customer_id: int):
    customer_id = db.execute_fetchone(sql_update_customer, (customer_id,))
    return customer_id

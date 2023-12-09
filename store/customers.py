from store.pdb import PDB
from models.Customer import Customer

db = PDB()

sql_select_customers = ''''''
sql_select_customer = ''''''
sql_update_customer = ''''''
sql_insert_customer = ''''''


def select_customers(filter_fio=None, is_finished=False):
    pass


def insert_customer(customer: Customer):
    pass


def select_customer_by_id(customer_id: int):
    pass


def update_customer_by_id(customer_id: int):
    pass

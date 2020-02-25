import sqlite3


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    #try:
    c = conn.cursor()
    c.execute(create_table_sql)
    #except Error as e:
    #    print(e)


def insertIntoMateriales(conn, material):
        sql = ''' INSERT INTO Materiales(code, name, sumTime, secStock, loteNum, level, unit)
              VALUES(?,?,?,?,?,?,?) '''
    

        cur = conn.cursor()
        cur.execute(sql, material)

        print(cur.lastrowid)
        conn.commit()


def insertIntoRadiadores(conn, radiador):
        sql = ''' INSERT INTO Radiadores(code, alum_id, alum_qty, tube_id, tube_qty, uses_lat, lat_qty, uses_turb, turb_qty, espesor)
          VALUES(?,?,?,?,?,?,?,?,?,?) '''
    

        cur = conn.cursor()
        cur.execute(sql, radiador)

        print(cur.lastrowid)
        conn.commit()


def insertIntoInvLote(conn, material):
        sql = ''' INSERT INTO InventarioLote(code, name, qty)
          VALUES(?,?,?) '''
    

        cur = conn.cursor()
        cur.execute(sql, material)

        print(cur.lastrowid)
        conn.commit()

def insertIntoInvSobr(conn, material):
        sql = ''' INSERT INTO InventarioSobrantes(code, name, qty, color)
            VALUES(?,?,?,?) '''
    

        cur = conn.cursor()
        cur.execute(sql, material)

        print(cur.lastrowid)
        conn.commit()

def insertIntoProdPlan(conn, prodPlanUnit):
    
        sql = ''' INSERT INTO PlanProduccion(code, month1, month2, month3, month4, month5, month6, month7, month8)
            VALUES(?,?,?,?,?,?,?,?,?) '''
    

        cur = conn.cursor()
        cur.execute(sql, prodPlanUnit)

        print(prodPlanUnit)
        conn.commit()
        

def insertIntoPedidos(conn, pedido):
    
        sql = ''' INSERT INTO Pedidos(name, code, qty, p_code, state, date_p, date_v, date_d, date_r, date_f)
            VALUES(?,?,?,?,?,?,?,?,?,?) '''
    

        cur = conn.cursor()
        cur.execute(sql, pedido)
        print(cur.lastrowid)

        conn.commit()
        
def insertIntoUsers(conn, user):

        sql = ''' INSERT INTO Pedidos(user, pass, type
            VALUES(?,?,?) '''
    

        cur = conn.cursor()
        cur.execute(sql, pedido)
        print(cur.lastrowid)

        conn.commit()
        

conn = sqlite3.connect('db.db')
 
sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Materiales (
                                    id integer PRIMARY KEY,
                                    code text NOT NULL,
                                    name text NOT NULL,
                                    sumTime text,
                                    secStock integer,
                                    loteNum integer,
                                    level integer, 
                                    unit text
                                ); """
                                
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Radiadores (
                                id integer PRIMARY KEY,
                                code integer NOT NULL,
                                alum_id integer NOT NULL,
                                alum_qty float NOT NULL,
                                tube_id text NOT NULL,
                                tube_qty float NOT NULL,
                                uses_lat text NOT NULL,
                                lat_qty text NOT NULL,
                                uses_turb text NOT NULL,
                                turb_qty text NOT NULL,
                                espesor float NOT NULL
                            );"""

sql_create_inventoryLote_table = """CREATE TABLE IF NOT EXISTS InventarioLote (
                                id integer PRIMARY KEY,
                                code integer NOT NULL,
                                qty integer NOT NULL
                            );"""

sql_create_inventorySobr_table = """CREATE TABLE IF NOT EXISTS InventarioSobrantes (
                                id integer PRIMARY KEY,
                                code integer NOT NULL,
                                name text NOT NULL,
                                qty integer NOT NULL,
                                color text NOT NULL DEFAULT 'En cuenta'
                            );"""

sql_create_prodPlan_table = """CREATE TABLE IF NOT EXISTS PlanProduccion (
                                id integer PRIMARY KEY,
                                code text NOT NULL,
                                month1 integer,
                                month2 integer,
                                month3 integer,
                                month4 integer,
                                month5 integer,
                                month6 integer,
                                month7 integer,
                                month8 integer
                            );"""

sql_create_pedidos_table = """CREATE TABLE IF NOT EXISTS Pedidos (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                code text NOT NULL,
                                qty integer NOT NULL,
                                p_code text NOT NULL,
                                state text NOT NULL,
                                date_p text NOT NULL,
                                date_v text,
                                date_d text,
                                date_r text
                            );"""

sql_create_users_table = """CREATE TABLE IF NOT EXISTS Pedidos (
                                id integer PRIMARY KEY,
                                user text NOT NULL,
                                pass text NOT NULL,
                                type text NOT NULL
                            );"""


## create projects table
#create_table(conn, sql_create_projects_table)
#
#
## create tasks table
#create_table(conn, sql_create_tasks_table)
#
## create inventory tables
create_table(conn, sql_create_inventoryLote_table)
#create_table(conn, sql_create_inventorySobr_table)

# create prod plan tables
#create_table(conn, sql_create_prodPlan_table)

# create pedidos table

#create_table(conn, sql_create_pedidos_table)

# create user table

create_table(conn, sql_create_users_table)

import pandas as pd

#radiadores = pd.read_csv('radiadores.csv')
#materiales = pd.read_csv('materiales.csv')
#inventario_lote = pd.read_csv('inventario_lote.csv')
#inventario_sobr = pd.read_csv('inventario_sobr.csv')
#prodPlan = pd.read_csv('prodPlan.csv', dtype = str)
#pedidos = pd.read_csv('pedidos_fabrica.csv')
#users = pd.read_csv('users.csv')

#for ad in range(0, int(radiadores.size/10)):
#    insertIntoRadiadores(conn, radiadores.values[ad])
##
#for ad in range(0, int(materiales.size/7)):
#    insertIntoMateriales(conn, materiales.values[ad])
##
#for ad in range(0, int(inventario_lote.size/3)):
#    insertIntoInvLote(conn, inventario_lote.values[ad])
##
#for ad in range(0, int(inventario_sobr.size/4)):
#    insertIntoInvSobr(conn, inventario_sobr.values[ad])
#
#for ad in range(0, int(prodPlan.size/9)):
#    insertIntoProdPlan(conn, prodPlan.values[ad])

#for ad in range(0, int(pedidos.size/10)):
#    insertIntoPedidos(conn, pedidos.values[ad])

#for ad in range(0, int(users.size/3)):
#    insertIntoUsers(conn, users.values[ad])



    






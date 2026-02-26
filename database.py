import sqlite3
import os
class CRUD:
    def __init__(self):
        self.conn = sqlite3.connect('myDB.db')
        self.cursor = self.conn.cursor()
        self.create_tables()


    def create_tables(self,):
        sql = '''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT

            );    
        '''
        self.cursor.execute(sql)

        sql = '''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cname TEXT NOT NULL,
                phone TEXT,
                photo TEXT
            );
        '''
        self.cursor.execute(sql)

        sql = '''
            CREATE TABLE IF NOT EXISTS factors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cid INTEGER NOT NULL,
                date TEXT NOT NULL,
                total INTEGER,
                FOREIGN KEY (cid) REFERENCES customers(id)
            );
        '''

        self.cursor.execute(sql)
        sql = '''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pname TEXT NOT NULL UNIQUE,
                price INTEGER NOT NULL
            );
        '''
        self.cursor.execute(sql)
        sql = '''
                CREATE TABLE IF NOT EXISTS factor_details (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fid INTEGER NOT NULL,
                    pid INTEGER NOT NULL,
                    price INTEGER NOT NULL,
                    no INTEGER NOT NULL,
                    subtotal INTEGER NOT NULL,
                    FOREIGN KEY (fid) REFERENCES factors(id),
                    FOREIGN KEY (pid) REFERENCES products(id)
                );
        '''
        self.cursor.execute(sql)

    def new_product(self,pname,price):
        sql =  "INSERT OR IGNORE INTO products (pname,price) VALUES (?,?)"
        val = (pname,price )
        self.cursor.execute(sql,val)
        self.conn.commit()

    def read_all_products(self):
        sql = "SELECT * FROM products"
        self.cursor.execute(sql)
        products = self.cursor.fetchall()
        return products
    
    
    def read_all_products_name(self,name):
        sql = "SELECT * FROM products WHERE pname = (?)" 
        val = (name,)
        self.cursor.execute(sql,val)
        products = self.cursor.fetchmany(5)
        return products
    
    def read_all_products_id(self,id):
        sql = "SELECT * FROM products WHERE id = (?)" 
        val = (id,)
        self.cursor.execute(sql,val)
        products = self.cursor.fetchmany(5)
        return products
    
    def add_new_costumer(self,name):
        sql = "INSERT INTO customers (cname)  VALUES  (?)"
        val = (name,)
        self.cursor.execute (sql,val)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def add_new_factor(self,cid,date,total):
        sql = "INSERT INTO factors (cid,date,total) VALUES (?,?,?)  "
        val = (cid,date,total)
        self.cursor.execute(sql,val)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_factor (self,factor_id,
                       total):
        sql = "UPDATE factors SET total = ? WHERE id = ?"
        val = (total,factor_id,)
        self.cursor.execute(sql,val)
        self.conn.commit()
        
    def del_factor(self,factor_id):
        sql = "DELETE FROM factors WHERE fid = ?"
        val =(factor_id,)   
        self.cursor.execute(sql,val)
        self.conn.commit()
        
    def add_factor_details(self,data_list):
        sql = "INSERT INTO factor_details (fid , pid , price , no ,subtotal ) VALUES(?,?,?,?,?)"
        self.cursor.executemany(sql,data_list)
        self.conn.commit()

    def del_factor_details(self,factor_id) :
        sql = "DELETE FROM factor_details WHERE fid = ?"
        val = (factor_id,)
        self.cursor.execute(sql,val)
        self.conn.commit()
    
    
    def read_factor_details(self,factor_id): # Cleaner ; Safer ; Updated
        sql = '''SELECT pid ,pname , factor_details.price , no , subtotal
        FROM products 
        JOIN factor_details
            ON factor_details.pid = products.id
          WHERE fid = ?
         
          '''
        val = (factor_id,)
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()
        
    def read_factor(self,factor_id,cname):
        sql = '''SELECT cid,customers.cname,factors.id,date,total
        FROM customers
        JOIN factors ON customers.id = factors.cid  
        WHERE factors.id = ?
        AND customers.cname = ?
        '''
        val = (factor_id,cname,)
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()
    
    def read_products_by_id_name(self,product_id,pname):
        sql = ''' SELECT  id, pname, price
        FROM products
        WHERE id = ?
        AND pname = ?
        '''
        val = (product_id,pname)
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()
        
    def read_costumer_by_id_name(self,cid,cname):
        sql = '''SELECT 
            customers.id,
            customers.cname,
            factor_details.fid,
            factor_details.pid
        FROM customers
        JOIN factors
            ON customers.id = factors.cid  
        JOIN factor_details
            ON factors.id = factor_details.fid
        WHERE customers.id = ?
            AND customers.cname = ?
        '''
        val = (cid,cname)
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()
    
    def read_username(self,uname):
        sql = '''SELECT 
        username 
        FROM user
        WHERE username = ?
        '''
        val = (uname,)
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()
    
    def read_username_pass(self,uname,password):
        sql = '''SELECT 
        username,password
        FROM user
        WHERE username = ?
        AND password = ?
        '''
        val = (uname,password)
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()

    def add_user_data(self,password,uname):
        sql = "INSERT INTO user (username , password ) VALUES(?,?)"
        val = (uname,password,)
        self.cursor.execute(sql,val)
        self.conn.commit()




if __name__ == "__main__":
    crud = CRUD()

    # print(crud.read_factor_details(29))
    # print(crud.read_factor(29,"hassan"))
    print(crud.read_factor(factor_id=1,cname="hassan"))
    print(crud.read_costumer_by_id_name(cid="3",cname="nazanin"))
    print(crud.read_username_pass(password="222",uname="adjkl"))
    print(crud.add_user_data(password="222",uname="adjkl"))
import psycopg2

def test_connect():
    connection = None
    # create a connection to the server and any database in it
    connection = psycopg2.connect(user = "postgres",
                                password = "postgres",
                                database = "postgres")

    if not connection == None:
        print("sucessfully connected")
        
        # if we have a connection, we can use a cursor to send querries to the database
        with connection.cursor()as cursor:
            cursor.execute("select * from orders")
            response = cursor.fetchall()
            print(response)
        
        
        
        # we can also send inserts, delete and stuff like that
        with connection.cursor() as cursor:
            cursor.execute("insert into orders (customer, status)"
                           " values('new customer', 'ordered'),"
                           " ('new customer1', 'ordered'),"
                           " ('new customer2', 'ordered')"
                           " returning id")
            connection.commit() #commit is always used to tell the server to save the changed we made
            response = cursor.fetchall()
            print(response)
            
        with connection.cursor() as cursor:
            cursor.execute("delete from orders where status = 'ordered'"
                           " returning id")
            connection.commit()
            response = cursor.fetchall()
            print(response)
        
        
    
        print("### Transaction with rollback")
        with connection.cursor()as cursor:
            cursor.execute("select * from orders")
            response = cursor.fetchall()
            print(response)   
            cursor.execute("BEGIN;") # like in terminal just send begin, to start a transaction
            cursor.execute("insert into orders (customer, status)"
                           " values('new customer', 'ordered'),"
                           " ('new customer1', 'ordered'),"
                           " ('new customer2', 'ordered')"
                           " returning id")
            response = cursor.fetchall()
            print(response)
            
            cursor.execute("select * from orders")
            response = cursor.fetchall()
            print(response)   
            
            cursor.execute("ROLLBACK;") # if something happend, or we don't want the changes send rollback
            
            cursor.execute("select * from orders")
            response = cursor.fetchall()
            print(response)   
            
            
            cursor.execute("insert into orders (customer, status)"
                           " values('new customer', 'ordered'),"
                           " ('new customer1', 'ordered'),"
                           " ('new customer2', 'ordered')"
                           " returning id")
            
            connection.commit() # after sending something else you can commit again
            cursor.execute("select * from orders")
            response = cursor.fetchall()
            print(response)  
            
    #you an also name a cursor and handle it's result line-by-line, item-by-item
    with connection.cursor(name="give_me_a_name") as cursor:
            cursor.execute("select * from orders")
            
            for line in cursor:
                for item in line:
                    print(item)
            
if __name__ == "__main__":
    test_connect()
    
    
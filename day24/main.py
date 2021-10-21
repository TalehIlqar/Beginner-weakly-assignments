import pymysql.cursors
import sys
connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             password='123456',
                             database='db',
                             charset = 'utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# *****************
# Table yaradilir
# *****************
if sys.argv[-2] == "create" and sys.argv[-1] == "table":
    def create_table():
        with connection.cursor() as cursor:
            sql = """
                create table if not exists book(
                    id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
                    title varchar(250) NOT NULL,
                    author varchar(250) NOT NULL,
                    added_in date NOT NULL,
                    price int NOT NULL,
                    exist boolean default true   
            )
            """
            cursor.execute(sql)
        connection.commit()
    create_table()




# *********************
# Table-a insert olunur
# *********************

if sys.argv[-2] == "add" and sys.argv[-1] == "book":  
    def create_book(title, author, added_in, price, exist):
        with connection.cursor() as cursor:
            sql = """
            insert into book(title, author, added_in, price, exist) values(%s, %s, %s, %s, %s)
            """
            cursor.execute(sql,(title, author, added_in, price, exist)) 
        connection.commit() 
    kitab_adi = input("kitabin adini daxil edin :")
    muellif = input("muellifin adini daxil edin :")
    qiymet = input("kitabin qiymetini daxil edin :")
    create_book(kitab_adi, muellif,  '2021-07-26', qiymet,  1 )









# **************
# Show all olur
# **************
if sys.argv[-2] == 'show' and sys.argv[-1] == 'all':
    def show_all():
        with connection.cursor() as cursor:
            sql = """
                select * from book 
            """
            cursor.execute(sql)
        return cursor.fetchall()

    print(show_all())


# *********************
# Book id-e gore oxunur
# *********************

if sys.argv[-2] == 'show' and sys.argv[-1] == 'book':
    def show_book(id):
        with connection.cursor() as cursor:
            sql = """
                select * from book where id = %s
            """
            cursor.execute(sql, (id))
        return cursor.fetchone()
    id_input = input("Kitab id-i yazin: ")
    print(show_book(id_input))



# *********************
# Status deyishir
# *********************

if sys.argv[-2] == "change" and sys.argv[-1] == "status":
    def change_status(id):
        with connection.cursor() as cursor:
                sql = """
                    update book set exist = not exist where id = %s
                """
                cursor.execute(sql, (id))
                connection.commit()
    use_id = input("deyismke istediyiniz kitabin ID-ni daxil edin :")
    change_status(use_id)



# *********************
# Qiymeti deyishir
# *********************

if sys.argv[-2] == "change" and sys.argv[-1] == "price":
    def change_price(id, price):
        with connection.cursor() as cursor:
                sql = """
                    update book  
                    set price = %s
                    where id = %s
                """
                cursor.execute(sql, (price, id))
        connection.commit()
    user_id = input("qiymetini deyismek istediyiniz kitabin ID-ni daxil edin :")
    price = input("yeni qiymeti daxil eidn : ")
    change_price(user_id, price)


# *********************
# Id-e gore setir silinir
# *********************

if sys.argv[-1] == "remove":
    def remove(id):
        with connection.cursor() as cursor:
                sql = """
                    delete from book
                    where id = %s
                """
                cursor.execute(sql, (id))
        connection.commit()
    user_id = input("qiymetini deyismek istediyiniz kitabin ID-ni daxil edin :")
    remove(user_id)


# *************************
# Sinvola gore line tapilir
# *************************
if sys.argv[-1] == "search":
    def search(like_word):
        with connection.cursor() as cursor:
            sql = f"""
                select * from book where title like '%{like_word}%' or author like '%{like_word}%' 
            """
            cursor.execute(sql)
            return cursor.fetchall()
    like_word = input("Herfi daxil edin: ")
    print(search(like_word))



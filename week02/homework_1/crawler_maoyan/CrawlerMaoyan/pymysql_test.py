import pymysql
import pymysql.cursors

DB_INFO = {
    'host': '172.30.53.17',
    'port': 3306,
    'user': 'root',
    'password': '<DB_PASSWORD>',
    'db': 'geekbangtrain_homework'
}

db_info = DB_INFO
print('DB_INFO is: ')
print(db_info)

db_host = db_info['host']
db_port = db_info['port']
db_user = db_info['user']
db_password = db_info['password']
db_name = db_info['db']
print('MySQLPipeline instantiated...')
connection = None
def open_spider():
    # conn = pymysql.connect(
    #     host = self.host,
    #     port = self.port,
    #     user = self.user,
    #     password = self.password,
    #     db = self.db
    # )
    connection = pymysql.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    print('DB connection opened...')
    print(connection)
    return connection

def process_item(connection, **db_info):
    cursor = connection.cursor()
    print(cursor)
    db_name = db_info['db']
    print(db_name)
    title = "['天气之子']"
    title = title.replace("'", r"\'")
    print(title)
    genre = '爱情／动画／奇幻'
    release_date = '2019-11-01'
    print(release_date)
    sql = f"INSERT INTO `{db_name}`.`maoyan_movie`(`movie_no`, `title`, `genre`, `release_date`) VALUES (NULL, '{title}', '{genre}', '{release_date}');"
    print(sql)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO `{db_name}`.`maoyan_movie`(`movie_no`, `title`, `genre`, `release_date`) VALUES (NULL, '{title}', '{genre}', '{release_date}');"
            cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = f"SELECT maoyan_movie.movie_no, maoyan_movie.title FROM maoyan_movie WHERE maoyan_movie.title = '{title}';"
            cursor.execute(sql, ('keraymondyan69@gmail.com',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

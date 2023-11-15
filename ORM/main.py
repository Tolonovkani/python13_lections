# ORM (Object-Relational Mapping) - технология прогаммирования, благодаря которой разработчики могут использовать язык программирования для взаимодействия с редяционной базой данных (PostgreSQL, MySQL, OracleDB). Вместо того чтобы писать сырые запросы на операторах SQL =, вы будете писать код ООП на языке программирования. Это очень сильно ускоряет разработку приложения и бд, особенно на начальных этапах.



from peewee import PostgresqlDatabase


db = PostgresqlDatabase(
    database='orm_db',
    user='kanybek',
    password='1',
    host='localhost',
    port=5432
)

# print(db.connect())
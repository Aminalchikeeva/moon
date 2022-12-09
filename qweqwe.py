# name = 'qwe'

# try:
#     print(name)
#     print(3/3)
#     print('1' + name)
# except (ZeroDivisionError, TypeError, NameError):
#     print('error')
# finally:
#     print('Программа завершена')


# try:
#     print(name)
#     print(3/3)
#     print('1' + name)
# except (ZeroDivisionError, TypeError, NameError):
#     print('error')
# finally:
#     print('Программа завершена')
    
# name = 'qwe'
# try:
#     print(name)
#     print(3/0)
#     print('1' + name)
# except (ZeroDivisionError, TypeError, NameError):
#     print('error')
# finally:
#     print('Программа завершена')

# name = 'qwe'

# try:
#     print(name)
#     print(3/0)
#     print('1' + name)
# except (ZNameError):
#     print('error')
# finally:
#     print('Программа завершена') 

# charfield стринговфй тип данных

from peewee import *
# import datetime
db = PostgresqlDatabase(
    'earth',
    port = '5432',
    host = 'localhost',
    user = 'air',
    password = 'qwe123',
)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db
        
class Company(BaseModel):
    name = CharField(max_lenght = 255, null=False, uniqe=True) 
    empolye_quantity = IntegerField()
    capital = IntegerField()
    owner = CharField(max_length = 255, null=False)
    
class Employee:
    Company = ForeignKeyField(Company, on_delete='CASCADE')
    email = CharField(max_length = 255, null=False)
    name = CharField(max_length = 255, null=False)
    second_name =CharField(max_length = 255, null=False)
    salary = IntegerField()
    
db.create_tables([Company, Employee])

db.close()

# Company.create(
#     name = 'Tesla',
#     Employee_quantity = 35,
#     capital = 300000,
#     owner = 'Elon Mask',
# )

# Company.create(
#     name ='apple',
#     Employee_quantity = 4000,
#     capital = 30000,
#     owner = 'steve Jobs'
# )


# Employee.create(
#     company = 1,
#     email = 'qwe123@gmail.com',
#     name = 'John',
#     second_name = 'Johnson',
#     salary = 10000,
# )


# Employee.create(
#     company = 1,
#     email = 'asdasd@gmail.com',
#     name = 'Aibek',
#     second_name = 'Aibek',
#     salary = 10000,
# )

# Employee.create(
#     company = 2,
#     email = 'qwerty@gmail.com',
#     name = 'Alex',
#     second_name = 'Alexandr',
#     salary = 5000,
# )

# Employee.create(
    # company = 2,
    # email = 'qweasd@gmail.com',
    # name = 'Aibek',
    # second_name = 'Aibekov',
    # salary = 70000,
# )

# db.close
# Ой а это код для базы данных в которую вносятся пользователи и их пароли.
# Вообще в идеале хранить не пароли а их кэш, кэшируя пароли при вводе их клиентами и сверяя эти кеши(ну и тавтология).
# Честно, почти не понимаю что тут происходит, коды ее и питоновские по бд это для меня дремучий лес, но вот в постгресе вроде чуток стал понимать.

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

sqlite_database = 'sqlite:///persons.db'
engine = create_engine(sqlite_database)
class Base(DeclarativeBase): pass
class Persons(Base): # Ну если не ошибаюсь мы тут табличку для имен пользователей создаем
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)

Base.metadata.create_all(bind=engine)

def create(usr_name, usr_passwrd):  # О а это знаю, тут мы создаем нового пользователя в табличку.
    with Session(autoflush=False, bind=engine) as db:
        # Проверяем, есть ли пользователь с таким именем.
        existing_user = db.query(Persons).filter_by(name=usr_name).first()
        if existing_user:
            print('Пользователь с таким именем уже существует.')
        else:   # Если нет такого то создаем.
            person = Persons(name=usr_name, password=usr_passwrd)
            db.add(person)
            db.commit()
            return existing_user

def authenticate(usr_name, usr_passwrd):    # Тут проверяем вводимые пользователям данные (совпадают логин и пароль или нет).
    with Session(autoflush=False, bind=engine) as db:
        existing_user = db.query(Persons).filter_by(name=usr_name).first()
        if existing_user and existing_user.password == usr_passwrd:
            return existing_user and existing_user.password == usr_passwrd
        else:
            return False



def all_persons():  # А вот эта штучка нужна по сути если понадобится вывести всех имеющихся пользователей.
    with Session(autoflush=False, bind=engine) as db:
        all_usrs = db.query(Persons)
        for k in all_usrs:
            print(f'{k.name}, {k.password}')

#Просто раскрыть текст ниже и вы увидите все содержащиеся логины и пароли в бд.
#(только не забудьте потом обратно закрыть, это работает как форточка и если открыто все пользователи как только запустят клиент так сразу увидят все логины и пароли).
#all_persons()


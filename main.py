from sqlalchemy import String,Integer,Column,create_engine

from sqlalchemy.orm import declarative_base,sessionmaker
import Repository

engine=create_engine("sqlite:///crud.db",echo=True)

base=declarative_base()

sessions=sessionmaker(bind=engine)
session=sessions()


class human(base):
    __tablename__="humans"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    family=Column(String)
    age=Column(Integer)
    def __init__(self,name="",family="",age=0):
        self.name=name
        self.family=family
        self.age=age

base.metadata.create_all(engine)

human1=human(name="ali",family="abasi",age=24)

repo=Repository.Repo()

repo.add(human1)


data=repo.Reed(human)
for item in data:
    print(item.name)
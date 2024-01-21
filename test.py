from sqlalchemy import create_engine,Column,String,Integer

from sqlalchemy.orm import sessionmaker,declarative_base


engine=create_engine("sqlite:///test.db",echo=True)


base=declarative_base()

sessions=sessionmaker(bind=engine)

session=sessions()


class human(base):
    __tablename__="humans"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    family=Column(String)
    def __init__(self,name="",family=""):
        self.name=name
        self.family=family
base.metadata.create_all(engine)

human1=human(name="pooriya",family="abasi")



alldata=session.query(human).all()


data=session.query(human).filter(human.id==1).first()

print(data.name)
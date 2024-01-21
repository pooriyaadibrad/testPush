from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///crud.db",echo=True)

sessions=sessionmaker(bind=engine)
session=sessions()
class Repo():
    def add(self,obj):
        session.add(obj)
        session.commit()
    def Reed(self,obj):

        return session.query(obj).all()
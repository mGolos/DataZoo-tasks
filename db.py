from time import mktime
from datetime import datetime, date, timedelta
from numpy.random import rand
from sqlalchemy import create_engine, Column, Integer, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class Weather(Base):
    '''Table to store JSON from "OpenWeatherMap API - Solar Radiation around the world".
    https://openweathermap.org/current.
    '''
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=date.today)
    json = Column(JSON, default='')

    def __str__(self):
        return self.output


def opendb():
    '''Create a connection with the database.
    '''
    engine = create_engine('sqlite:///db.sqlite3')
    Session = sessionmaker(bind=engine)
    return Session()


def create_random_data(N=10):
    '''Delete all possible elements and create a new set of size N.
    Values are randomly defined around arbitrary values.
    '''
    db = opendb()
    db.query(Weather).delete()
    db.commit()
    
    timedate = datetime.now()
    
    for _ in range(N):
        json = '{"coord": {'\
            f'"lon":{(rand()-.5)*360:.4f},\
            "lat": {(rand()-.5)*180:.4f}'\
            '},"list": [{"radiation": {'\
            f'"ghi": {rand()*30:.2f},'\
            f'"dni": {rand()*3:.2f},'\
            f'"dhi": {rand()*300:.2f},'\
            f'"ghi_cs": {rand()*1000:.2f},'\
            f'"dni_cs": {rand()*1000:.2f},'\
            f'"dhi_cs": {rand()*150:.2f}'\
            '},'f'"dt": {mktime(timedate.timetuple())}''}]}'
            
        rad = Weather(date=timedate.date(), json=json)
        db.add(rad)    
        
    db.commit()
    db.close()
    return True


engine = create_engine('sqlite:///db.sqlite3', echo=True)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_random_data(10)
# or instead we could use an ORM like sql alchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from pymysql import *



#GOOD way to take user input, NOT vulnerbale to Injection Attack

#better way
from dotenv import load_dotenv
import os

load_dotenv("my_credentials.env")
#ADD my_credentials.env to .gitignore, or just add all .env files to .gitignore

db_user=os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host=os.getenv("DB_HOST")
db_name=os.getenv("DB_NAME")

Base= declarative_base()

#Define ORM model (this replaces the previous CREATE TABLE logic)
class Player(Base):
    __tablename__ = "players"
    playerID = Column(Integer,primary_key=True)
    firstname = Column(String(255),nullable=False)
    lastname = Column(String(255), nullable=False)
    sport = Column(String(255),nullable=False)


try:
    engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                           echo=False) # set True for generated SQL
    
    #drop players first
    Base.metadata.drop_all(
    engine,
    tables=[Player.__table__],
    checkfirst=True
    )
    
    #create tables if they don't exist
    Base.metadata.create_all(engine)

    #Create session (replaced cursor)
    Session = sessionmaker(bind=engine)
    session= Session()

    print("Connected using SQLAlchemy")

    #Insert example
    serena = Player(firstname="Serena",lastname="Williams",sport="Tennis")
    session.add(serena)
    session.commit()

    while True:
        check = input("do you want to add a player to the database? (y,n)")
        if check != "y":
            break

        playerID = int(input("Enter player ID:"))
        firstname = input("Enter player first name:")
        lastname = input ("Enter player last name:")
        sport = input ("Enter player's sport")

        new_player = Player(
            playerID= playerID,
            firstname = firstname,
            lastname = lastname,
            sport = sport
        )

        session.add(new_player)
        session.commit()
    
    
    players = session.query(Player).all()

    for player in players:
        print(player.playerID, player.firstname, player.lastname, player.sport)

    session.close()
    engine.dispose()
       
except SQLAlchemyError as e:
    print("Database error:", e)


#allow user to to add a player

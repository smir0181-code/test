from sqlalchemy import*
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import String
engine=create_engine('sqlite:///database.db')
metadata=MetaData()
users=Table('users',metadata,autoload_with=engine)
conn=engine.connect()
result=conn.execute(select(users))
all_users=result.fetchall()
print(*all_users,sep='\n')

import sqlalchemy as db
import pandas as pd
from bugsnax import *

bugsnax_dict = get_bugsnax()
location_dict = get_location()
grumpus_dict = get_grumpus()

bugsnax_df = pd.DataFrame.from_records(bugsnax_dict, exclude=['location'])
location_df = pd.DataFrame.from_records(location_dict, 
                                        exclude=['bugsnax', 'inhabitants'])
grumpus_df = pd.DataFrame.from_records(grumpus_dict, 
                                       exclude=['fears', 'hates', 'locations', 'loves'])

engine = db.create_engine('sqlite:///bugsnax_db.db')

bugsnax_df.to_sql('bugsnak', con=engine, if_exists='replace', index=False)
location_df.to_sql('location', con=engine, if_exists='replace', index=False)
grumpus_df.to_sql('grumpus', con=engine, if_exists='replace', index=False)

bug_q = engine.execute("SELECT * FROM bugsnak").fetchall()
print(pd.DataFrame(bug_q))

location_q = engine.execute("SELECT * FROM location").fetchall()
print(pd.DataFrame(location_q))

grump_q = engine.execute("SELECT * FROM grumpus").fetchall()
print(pd.DataFrame(grump_q))

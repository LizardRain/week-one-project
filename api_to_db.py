import sqlalchemy as db
import pandas as pd
from bugsnax import *

bugsnax_dict = get_bugsnax()

bugsnax_df = pd.DataFrame.from_records(bugsnax_dict, exclude=['location'])

engine = db.create_engine('sqlite:///bugsnax_db.db')

bugsnax_df.to_sql('bugsnak', con=engine, if_exists='replace', index=False)

query_result = engine.execute("SELECT * FROM bugsnak").fetchall()
print(pd.DataFrame(query_result))



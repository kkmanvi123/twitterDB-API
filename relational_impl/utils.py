import pandas as pd
import psycopg2


class utils:
    def __init__(self, user, password, database, host="localhost"):
        """ connect to db """
        self.con = psycopg2.connect(
            user=user,
            password=password,
            database=database,
            host=host
        )

    def close(self):
        """ close a connection """
        self.con.close()
        self.con = None

    def execute(self, query):
        """ execute select query, return as df """

        # Step 1: Create cursor
        cur = self.con.cursor()

        # Step 2: Execute the query
        cur.execute(query)

        # Step 3: Get the resulting rows and column names
        rows = cur.fetchall()
        cols = [desc[0] for desc in cur.description]

        # Step 4: Close the cursor
        cur.close()

        # Step 5: Return result
        return pd.DataFrame(rows, columns=cols)

    def insert_one(self, sql, val):
        """ insert a row """
        cur = self.con.cursor()
        cur.execute(sql, val)
        self.con.commit()

    def insert_many(self, sql, vals):
        """ insert multiple rows """
        cur = self.con.cursor()
        cur.executemany(sql, vals)
        self.con.commit()

# conn = psycopg2.connect(
#     user=os.environ["postgres_user"],
#     password=os.environ["postgres_password"],
#     host='localhost',
#     database='twitterDB'
# )

# cursor = con.cursor()
# cursor.execute('SELECT * FROM follows WHERE follows_id=1;')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

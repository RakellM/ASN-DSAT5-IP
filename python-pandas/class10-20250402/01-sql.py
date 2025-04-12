# %%

import pandas as pd
import os
import sqlalchemy

# %%

os.chdir(r"C:\Users\kel_m\OneDrive\Nerd_Code\DSAT5-IP\python-pandas")

os.getcwd()

# %%

engine = sqlalchemy.create_engine("sqlite:///./data/olist.db")

df = pd.read_sql_table("tb_customers", engine)

# %%

df.head()

# %%

df_transaction = pd.read_sql_table("tb_order_items", engine)
df_transaction.head()

# %%

df_summary_seller = (df_transaction.groupby("seller_id")["order_id"]
                                   .count()
                                   .reset_index())

# %%

query = """
SELECT 
    seller_id ,
    count(*) AS qtySales
FROM tb_order_items
GROUP BY 1 ;
"""

# %%

df_summary = pd.read_sql_query(query, engine)



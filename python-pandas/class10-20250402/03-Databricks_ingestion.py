# %%

spark.table("silver.olist.vendedor").display()

# %%

query = """
SELECT 
    idVendedor , 
    count(*) AS frequency ,
    sum(vlPreco) AS amount
FROM silver.olist.item_pedido
GROUP BY 1
"""

df1 = spark.sql(query).display()
df1

# %%

with open ("fs_avaliacao.sql") as open_file:
    query = open_file.read()

print(query)

# %%

print(query.format(date="2017-05-01"))

# %%

df = spark.sql(query.format(date="2017-05-01"))
df

# %%

with open ("fs_avaliacao.sql") as open_file:
    query = open_file.read()

def ingest_table_cohort(query, table, cohort):
    df = spark.sql(query.format(date=cohort))

    spark.sql(f"""DELETE FROM sandbox.asn.{table} WHERE dtRef = '{cohort}'""")

    (df.write
       .mode("append")
       .format("delta")
       .saveAsTable(f"sandbox.asn.{table}"))
    
ingest_table_cohort(query=query, table="fs_seller_avaliacao_t5", cohort="2017-07-01")

# %%

%sql

SELECT dtRef, COUNT(*) FROM sandbox.asn.fs_seller_avaliacao_t5 GROUP BY ALL

# %%

import datetime as dt

start = "2017-01-01"
stop = "2018-01-01"

def date_range(start, stop, monthly=False):
    dates = []
    while start <= stop:
        dates.append(start)
        dt_ = dt.datetime.strptime(start, "%Y-%m-%d") + dt.timedelta(days=1)
        start = dt_.strftime("%Y-%m-%d")

    if monthly:
        return [i for i in dates if i.endswith("-01")]
    
    return dates

date_range("2017-01-01", "2017-05-10", monthly=True)

# %%

# Final code - P1
import datetime as dt

start = "2017-01-01"
stop = "2018-01-01"

def date_range(start, stop, monthly=False):
    dates = []
    while start <= stop:
        dates.append(start)
        dt_ = dt.datetime.strptime(start, "%Y-%m-%d") + dt.timedelta(days=1)
        start = dt_.strftime("%Y-%m-%d")

    if monthly:
        return [i for i in dates if i.endswith("-01")]
    
    return dates

def ingest_table_cohort(query, table, cohort):
    df = spark.sql(query.format(date=cohort))

    try:
        spark.sql(f"""DELETE FROM sandbox.asn.{table} WHERE dtRef = '{cohort}'""")
        (df.write
        .mode("append")
        .format("delta")
        .saveAsTable(f"sandbox.asn.{table}"))
    except Exception as e:
            (df.write
               .mode("overwrite")
               .option("overwriteSchema", "true")
               .format("delta")
               .saveAsTable(f"sandbox.asn.{table}"))
    

# %%

# Final code - P2
start = "2017-01-01"
stop = "2018-01-01"
table = "fs_avaliacao"

dates = date_range(start=start, stop=stop, monthly=True)

with open (f"{table}.sql") as open_file:
    query = open_file.read()

for i in dates:
    ingest_table_cohort(query=query, table=f"{table}_t5", cohort=i)
    
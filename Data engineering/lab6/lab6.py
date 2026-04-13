import duckdb
import pandas as pd
import json

# ex 0
with open('lab6_params.json', 'r') as f:
    config = json.load(f)

con = duckdb.connect("lab6.duckdb")


con.sql(f"CREATE OR REPLACE TABLE readings AS SELECT * FROM '{config['dataset']}'")




# ex 1
df_ex1 = con.sql("SELECT count(DISTINCT detector_id) FROM readings").df()
df_ex1.to_pickle("lab6_ex01_detector_no.pkl")


# ex 2

df_ex2 = con.sql("""
    SELECT 
        detector_id,
        count(count),
        min(starttime),
        max(starttime)
    FROM readings
    GROUP BY detector_id
    ORDER BY detector_id
""").df()
df_ex2.to_pickle("lab6_ex02_detector_stat.pkl")


# ex 3

df_ex3 = con.sql("""
    SELECT
        detector_id,
        count,
        LAG(count) OVER (PARTITION BY detector_id ORDER BY starttime)
    FROM readings
    WHERE detector_id = 146
    ORDER BY starttime
    LIMIT 500
""").df()
df_ex3.to_pickle("lab6_ex03_detector_146_lag.pkl")


# ex 4

df_ex4 = con.sql("""
    SELECT
        detector_id,
        count,
        SUM(count) OVER (
            PARTITION BY detector_id 
            ORDER BY starttime 
            ROWS BETWEEN CURRENT ROW AND 9 FOLLOWING
        )
    FROM readings
    WHERE detector_id = 146
    ORDER BY starttime
    LIMIT 500
""").df()
df_ex4.to_pickle("lab6_ex04_detector_146_sum.pkl")


# ex 5


df_ex5 = con.sql("""
    SELECT
        detector_id,
        starttime,
        count,
        SUM(count) OVER (
            PARTITION BY detector_id 
            ORDER BY starttime 
            RANGE BETWEEN CURRENT ROW AND INTERVAL 900 SECONDS FOLLOWING
        )
    FROM readings
    WHERE detector_id = 146
    ORDER BY starttime
    LIMIT 500
""").df()
df_ex5.to_pickle("lab6_ex05_detector_146_sum.pkl")


# Zamknięcie połączenia
con.close()
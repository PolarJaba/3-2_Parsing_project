import requests
import psycopg2

# connection parameters
host = 'postgres'
port = '5432'
username = 'show'
password = '1238'
database = 'dbtest'

# connection
connection = psycopg2.connect(
    host=host,
    port=port,
    user=username,
    password=password,
    database=database
)

# parsing
url = 'https://api.exchangerate.host/timeseries?start_date=2020-01-01&end_date=2020-01-31&base=BTC&symbols=RUB'
response = requests.get(url)
data = response.json()

# data checking
print(data)

# working tuple creating
lst = []
cur1 = data['base']
for dates in data['rates']:
    for cur2 in data['rates'][dates]:
        lst.append(tuple([dates, cur1, cur2, data['rates'][dates][cur2]]))
print(lst)

# creating table containing parsing data
with connection.cursor() as cur:
    query_create = "CREATE TABLE IF NOT EXISTS public.parsing_data(rate_id serial PRIMARY KEY, cur_date DATE NOT " \
                   "NULL, currency1 VARCHAR(3) NOT NULL, currency2 VARCHAR(3) NOT NULL, rate_1_to_2 FLOAT );"
    cur.execute(query_create)
    cur.executemany("INSERT INTO public.parsing_data(cur_date, currency1, currency2, rate_1_to_2) VALUES(%s,"
                    "%s, %s, %s);", lst)
    connection.commit()
    cur.close()

# creating data queries and data mart
with connection.cursor() as cur:
    cur.execute("SELECT CAST(date_part('month', cur_date) AS BIGINT) AS cur_month, currency1, currency2, cur_date AS"
                "date_max, rate_1_to_2 AS max_rate FROM parsing_data " 
                "WHERE rate_1_to_2 = (SELECT MAX(rate_1_to_2) FROM parsing_data)")
    data_max = cur.fetchone()

    cur.execute("SELECT cur_date AS date_min, rate_1_to_2 AS min_rate " 
                "FROM parsing_data WHERE rate_1_to_2 = (SELECT MIN(rate_1_to_2) FROM parsing_data)")
    data_min = cur.fetchone()

    cur.execute("SELECT AVG(rate_1_to_2) AS average FROM parsing_data")
    data_avg = cur.fetchone()

    cur.execute("SELECT rate_1_to_2 AS last_rate FROM parsing_data WHERE cur_date = CAST(date_trunc('month', "
                "cur_date) + INTERVAL '1 month - 1 day' AS DATE)")
    data_last_day = cur.fetchone()

    res = (data_max + data_min + data_avg + data_last_day)

    # result data check
    print(res, type(res), len(res))

    # creating and containing data mart
    cur.execute("CREATE TABLE IF NOT EXISTS public.parsing_data_mart(cur_month BIGINT, currency1 VARCHAR(3) NOT NULL,"
                "currency2 VARCHAR(3) NOT NULL, date_max DATE, max_rate FLOAT,  date_min DATE, min_rate FLOAT,"
                "avg_rate FLOAT, last_month_day_rate FLOAT);")
    cur.execute("INSERT INTO public.parsing_data_mart(cur_month, currency1, currency2, date_max, max_rate, date_min," 
                "min_rate, avg_rate, last_month_day_rate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);", res)
    connection.commit()
    cur.close()
connection.close()
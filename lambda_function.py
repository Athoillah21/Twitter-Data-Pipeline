import json
import psycopg2

ENV='dev'

credential = {
    'dbname': '*****',
    'port': '*****',
    'user': '*****',
    'password': '*****',
    'host_url': '*****'
}

REDSHIFT_ROLE = {
    'dev': '*****'
}

BUCKET = {
    'dev': '*****'
}

def lambda_handler(event, context):
    conn_string = "dbname='{}' port='{}' user='{}' password='{}' host='{}'".format(credential['dbname'],credential['port'],credential['user'],credential['password'],credential['host_url'])
    print(conn_string)
    con = psycopg2.connect(conn_string)
    cur = con.cursor()
    print(con)
    
    # bucket = event["Records"][0]["s3"]["bucket"]["name"]
    # key = event["Records"][0]["s3"]["object"]["key"]
    
    bucket='*****'
    key='*****'
    
    sql_file="s3://"+bucket+"/"+key
    
    sql_query="""copy twitter.data
    from '{0}'
    iam_role '{1}'
    delimiter ','
    IGNOREHEADER as 1
    csv;""".format(sql_file,REDSHIFT_ROLE['dev'])
    print(sql_query)
    cur.execute("truncate table dev.twitter.data")
    cur.execute(sql_query)

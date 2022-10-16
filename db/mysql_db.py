import mysql.connector.pooling

__config = {
    "host":"192.168.42.13",
    "port":3308,
    "user":"root",
    "password":"123456",
    "database":"vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)
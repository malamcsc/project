#PG_HOSTED_ON = "local" # Use "local" or "azure" for auth method switch.

# DB_PGNAME = 'localhost'     # PostgreSQL server name
# DB_PORT = '5432'         # PostgreSQL server port
# DB_UNAME = 'postgres'       # PostgreSQL user name
# DB_PWD = 'root12'           # PostgreSQL user password

DB_PGNAME = 'api-db-test'     # PostgreSQL server name
DB_PORT = '5432'         # PostgreSQL server port
DB_UNAME = 'malamcsc'       # PostgreSQL user name
DB_PWD = 'Patna@123'           # PostgreSQL user password


pgsql_connection_string = "postgres://"+DB_UNAME+"%40"+DB_PGNAME+":"+DB_PWD+"@"+DB_PGNAME+".postgres.database.azure.com"+":"+DB_PORT+"/"

#pgsql_connection_string = "postgres+psycopg2://"+DB_UNAME+":"+DB_PWD+"@"+DB_PGNAME+":"+DB_PORT+"/"
                                

SQLALCHEMY_BINDS = {
    "test_api": pgsql_connection_string+"test_api"
}
#PG_HOSTED_ON = "local" # Use "local" or "azure" for auth method switch.

# DB_PGNAME = 'localhost'     # PostgreSQL server name
# DB_PORT = '5432'         # PostgreSQL server port
# DB_UNAME = 'postgres'       # PostgreSQL user name
# DB_PWD = 'root12'           # PostgreSQL user password

DB_PGNAME = 'api-db-test.postgres.database.azure.com'     # PostgreSQL server name
DB_PORT = '5432'         # PostgreSQL server port
DB_UNAME = 'malamcsc@api-db-test'       # PostgreSQL user name
DB_PWD = 'Patna123'           # PostgreSQL user password

pgsql_connection_string = "postgres://"+DB_UNAME+":"+DB_PWD+"@"+DB_PGNAME+:"+DB_PORT+"/"

                                

SQLALCHEMY_BINDS = {
    "test_api": pgsql_connection_string+"test_api"
}

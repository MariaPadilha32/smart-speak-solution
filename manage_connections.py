import psycopg2

# Database connection parameters
dbname = 'chomp_junky_vapor_511024'
user = 'ucohxgsjtci'
password = '5qL1xcxQPO3o'
host = 'ep-gentle-mountain-a23bxz6h.eu-central-1.aws.neon.tech'
port = '5432'

# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    conn.autocommit = True
    cursor = conn.cursor()

    # Query to check active connections
    check_connections_query = """
    SELECT pid, usename, client_addr, datname, query, state
    FROM pg_stat_activity
    WHERE state = 'active';
    """
    cursor.execute(check_connections_query)
    active_connections = cursor.fetchall()
    print("Active connections:")
    for connection in active_connections:
        print(connection)

    # Query to terminate idle connections
    terminate_idle_query = """
    SELECT pg_terminate_backend(pid)
    FROM pg_stat_activity
    WHERE state = 'idle' AND usename = %s;
    """
    cursor.execute(terminate_idle_query, (user,))
    print("Terminated idle connections")

    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")


import cx_Oracle

def connect_to_oracle(server, port, userid, password, sid=None, service_name=None):
    # Construct the connection string
    dsn = cx_Oracle.makedsn(server, port, sid=sid, service_name=service_name)
    
    # Establish a connection to the Oracle database
    connection = cx_Oracle.connect(user=userid, password=password, dsn=dsn)
    
    return connection

# Database connection details
database_server = "your_database_server"
database_port = "your_database_port"
database_userid = "your_username"
database_password = "your_password"
database_sid = "your_sid"  # Use this if connecting using SID
database_service_name = "your_service_name"  # Use this if connecting using service name

# Connect to the Oracle database
try:
    connection = connect_to_oracle(
        server=database_server,
        port=database_port,
        userid=database_userid,
        password=database_password,
        sid=database_sid,
        service_name=database_service_name
    )

    # Now you can perform database operations using the 'connection' object
    
    # For example:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

finally:
    # Close the connection when done
    connection.close()

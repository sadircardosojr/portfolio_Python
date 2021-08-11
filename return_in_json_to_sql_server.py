import pyodbc as pyodbc

def getData():
    
    server = "YOUR_SERVER"
    database = "YOUR_DB"
    username = "YOUR_USER_NAME"
    password = "YOUR_PASSWORD"
    driver = "{ODBC Driver 17 for SQL Server}"
    print('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=********')

    cnxn = pyodbc.connect('DRIVER='
        +driver+
        ';SERVER='
        +server+
        ';DATABASE='
        +database+
        ';UID='
        +username+
        ';PWD='
        + password)

    query = """
    select  * from YOUR_TABLE 
    FOR JSON AUTO
    """
    
    cnxn.timeout = 15       
    cursor = cnxn.cursor()
    cursor.execute(query)
    
    return_query = ""

    for row in cursor:
        return_query = return_query + str(row[0])
        
    return return_query

if __name__ == '__main__':
    retorno = str(getData())

    print("\n RETORNO: " + retorno)

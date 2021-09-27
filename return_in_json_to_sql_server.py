import pyodbc as pyodbc

def getData():
    
    server = "YOUR_SERVER"
    database = "YOUR_DB"
    username = "YOUR_USER_NAME"
    password = "YOUR_PASSWORD"
    driver = "{ODBC Driver 17 for SQL Server}"
    print('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=********')

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
    select  [columns] from YOUR_TABLE 
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
https://prod.liveshare.vsengsaas.visualstudio.com/join?DBF00F2EF6B9BDD8BCC5B44360DA7444FB95

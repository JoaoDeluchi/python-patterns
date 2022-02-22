PROVIDER = 'sql_server'

CONNSTR = (
    'DRIVER={SQL Server};' +
    'SERVER=.\\sql2019;' +
    'DATABASE=EXAMPLE;' +
    'TRUSTED_CONNECTION=TRUE;'
)

QUERY = '''
    SELECT DISTINCT TOP 5 FirstName, LastName
    FROM Person.Person
    ORDER by LastName, FirstName;
'''

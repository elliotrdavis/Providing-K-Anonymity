import pymysql
import pandas as pd
from DimensionTables import dimensionTables, indexTables
from sqlalchemy import create_engine

# This class imports data from my SQL database and converts it into
# a pandas dataframe
# https://appdividend.com/2020/04/27/python-pandas-how-to-convert-sql-to-dataframe/

host = 'localhost'
user = 'root'
password = 'root'
database = 'kanonymity'


def importTable():
    dbcon = pymysql.connect(host=host, user=user, password=password, database=database)

    try:
        SQL_Query = pd.read_sql_query('''select * from voterlist''', dbcon)

        VoterListColumns = ['VoterID', 'Name', 'Age', 'Sex', 'Address', 'Party', 'Postcode']
        VoterListDF = pd.DataFrame(SQL_Query, columns=VoterListColumns)
        print(VoterListDF)
        # print('The data type of df is: ', type(VoterListDF))

    except:
        print("Error: unable to fetch data")

    dbcon.close()


def dimTableToSQL():
    dimensionTables()

    # print(dimensionTables.postcodeDF0)

    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db=database))

    dimensionTables.partyDF0.to_sql('partysql0', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.nameDF0.to_sql('namesql0', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.nameDF1.to_sql('namesql1', con=engine, if_exists='replace', chunksize=1000)

    dimensionTables.addressDF0.to_sql('addresssql0', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.addressDF1.to_sql('addresssql1', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.ageDF0.to_sql('agesql0', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.ageDF1.to_sql('agesql1', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.ageDF2.to_sql('agesql2', con=engine, if_exists='replace', chunksize=1000)

    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db="sex"))
    dimensionTables.sexDF0.to_sql('sexsql0', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.sexDF1.to_sql('sexsql1', con=engine, if_exists='replace', chunksize=1000)

    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db="postcode"))
    dimensionTables.postcodeDF0.to_sql('postcodesql0', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.postcodeDF1.to_sql('postcodesql1', con=engine, if_exists='replace', chunksize=1000)
    dimensionTables.postcodeDF2.to_sql('postcodesql2', con=engine, if_exists='replace', chunksize=1000)


def uploadIndexTables():
    indexTables()
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db="dimindex"))

    indexTables.partyDimDF.to_sql('party', con=engine, if_exists='replace', chunksize=1000)
    indexTables.nameDimDF.to_sql('name', con=engine, if_exists='replace', chunksize=1000)
    indexTables.sexDimDF.to_sql('sex', con=engine, if_exists='replace', chunksize=1000)
    indexTables.addressDimDF.to_sql('address', con=engine, if_exists='replace', chunksize=1000)
    indexTables.ageDimDF.to_sql('age', con=engine, if_exists='replace', chunksize=1000)
    indexTables.postcodeDimDF.to_sql('postcode', con=engine, if_exists='replace', chunksize=1000)


def readSQL():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    my_cursor = connection.cursor()

    # Execute Query
    my_cursor.execute("SELECT * from agesql2")

    # Fetch the records
    result = my_cursor.fetchall()

    for i in result:
        print(i)

    connection.close()


# def generateNodes():
#     connection = pymysql.connect(host=host, user=user, password=password, database=database)
#
#     my_cursor = connection.cursor()
#
#     # Execute Query
#     my_cursor.execute("SELECT * from agesql2")
#
#     # Fetch the records
#     result = my_cursor.fetchall()
#
#     for i in result:
#         print(i)
#
#     connection.close()

# Node generation
# INSERT INTO Ci(dim1, index1,..., dimi, indexi, parent1, parent2)
# SELECT p.dim1, p.index1,..., p.dimi−1, p.indexi−1, q.dimi−1, q.indexi−1, p.ID, q.ID
# FROM Si−1 p, Si−1 q
# WHERE p.dim1 = q.dim1 ∧ p.index1 = q.index1 ∧ ...
# ∧ p.dimi−2 = q.dimi−2 ∧ p.indexi−2 = q.indexi−2
# ∧ p.dimi−1 < q.dimi−1

# Where
# Ci: i = quasi-identifier size, C = candidate nodes
# dimi = quasi identifer columns
# index = level in dimi table

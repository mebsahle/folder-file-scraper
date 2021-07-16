import os
import sqlite3

try:
    sqliteConnection = sqlite3.connect('../folder_to_db/SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    os.chdir('../folder_to_db/files')
    dir_loc = os.getcwd()
    list_of_dir = list(os.listdir(dir_loc))
    ## print("PWD, ",os.getcwd(), dir_loc)
    
    cnt = 0
    # create table if not exists ark_file (id integer PRIMARY KEY, name text not NULL);
    for file in list_of_dir:
        ## print("ey...",file)
        if file.split('.')[1] == 'ark': # can be changed to the file extension you wish to be selected
            ## print('hey', file.split('.')[0])
            file_metadata = (file.split('.')[0])
            sqlite_insert_Query = "INSERT INTO ark_file (id, name) VALUES (?,?)"
            data = (cnt, str(dir_loc+'/'+file))
            print("ey",data)
            #cursor.execute(sqlite_insert_Query)
            count = cursor.execute(sqlite_insert_Query, data)
            sqliteConnection.commit()
        cnt+=1
    print("Database created and Successfully Connected to SQLite")
    
    print("SQLite Database Version is: ", count)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

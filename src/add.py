import sqlite3
import os
import datetime

def add(message):
    arg = message.spilt(' ')

    con = sqlite3.connect('./data/todo.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE todo(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,title VARCHAR(100) NOT NULL,description TEXT NULL,created DATETIME NOT NULL,deadline DATETIME NOT NULL,start INT CHECK (start between 0 and 2) );")
    
    default = {'title', 'description', 'deadline', 0} 

    #print(f'This app is a todo app for Command Line Interface')
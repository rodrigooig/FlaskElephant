import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='suleiman.db.elephantsql.com',
                            database='iywkoszh',
                            user=os.environ['iywkoszh'],
                            password=os.environ['SUkfBFgPhRw1QknhVW5YZSMYGwoBNo-b'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)


app.run(host='0.0.0.0', port=81)

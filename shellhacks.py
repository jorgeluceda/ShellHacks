from flask import Flask, render_template
# from flask_mysqldb import MySQL

app = Flask(__name__)


nav_data = {
    'categories' : ['Math', 'Computer Science', 'English']
}

@app.route('/')
def homepage():
    return render_template('index.html', data=nav_data)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')

    '''
        cur = mysql.connection
        app.run(host='0.0.0.0')
    
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'matheus'
        app.config['MYSQL_PASSWORD'] = 'jovem'
        app.config['MYSQL_DB'] = 'unibooks'
    '''
        # cur = mysql.connection.cursor()
    
        # cur.execute(CREATE DATABASE book)
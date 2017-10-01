from flask import Flask, render_template
# from flask_mysqldb import MySQL

nav_categories = ['All', 'Math', 'Computer Science', 'English']


nav_directories = ['all', 'math', 
                    'cs', 'english']


app = Flask(__name__)




@app.route('/')
def homepage():
    return render_template('index.html', cats=nav_categories,
            dirs=nav_directories, hover="All")

@app.route('/all')
def all():
    return render_template('all.html', cats=nav_categories,
            dirs=nav_directories, hover=nav_categories[0])
    
@app.route('/math')
def math():
    return render_template('math.html', cats=nav_categories,
            dirs=nav_directories, hover=nav_categories[1])
    
@app.route('/cs')
def cs():
    return render_template('cs.html', cats=nav_categories,
            dirs=nav_directories, hover=nav_categories[2])

@app.route('/english')
def english():
    return render_template('english.html', cats=nav_categories,
            dirs=nav_directories, hover=nav_categories[3])
    
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
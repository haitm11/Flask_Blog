from flask import Flask, render_template, redirect, url_for, request
import pymysql.cursors
 
app = Flask(__name__)
 

def getConnection():
	connection = pymysql.connect(host='127.0.0.1', user='root', password='minhanh11', db='job_demo',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	return connection

@app.route('/')
def welcome():
    return redirect('/job')
 
 
# Route for handling the login page logic
"""@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
    	#name = request.form['username']
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', ER=error)"""

@app.route('/job', methods=['GET', 'POST'])
def job():
	jobname = None
	value = None
	if request.method == 'POST':
		jobname = request.form['jobname']
		connection = getConnection()
		try:
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM TEST WHERE job_title=(%s)", [jobname])
			value = cursor.fetchall()
		finally:
			connection.close()
	return render_template('jobsearch.html', ER=value)
 
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
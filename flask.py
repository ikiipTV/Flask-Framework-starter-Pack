from flask import Flask
from flask import render_template
from flask import url_for
from flask import sqlite3
app = Flask(__name__)

#initialize the application
#adding the application routes
@app.route('/')
def index():
    return render_template("index.html")
    #this can also be written to return a plain text
    #for example (return "hello world")
@app.route('/about')
def about-us():
    return render_template("about-us.html")
    
    #this should display results gotten from the add-result function
@app.route('/result', method=['post','get'])
def result():
    if request.form == 'post':
        result = request.form
        return render_template('result.html', result=result)
        
        #this should redirect to the result() function
 @app.route('/enterscores')
 def add-result():
     return render_template('addresult.html')
     
     #this should store user details in the database
@app.route('/addrec' method=['post','get'])
def addrec():
    if request.form == 'post':
        try:
            nm = request.form['nm']
            password = request.form['password']
            loc = request.form['loc']
            occ = request.form['occ']
            
            with sql.connect(database.db) as conn:
            cur = conn.cursor
            cur.execute("insert into students(name,password,loc,occ) values(?,?,?,?)"(nm,password,loc,occ))
            #commit the details
            conn.commit()
            msg = "details inserted successfully"
        except:
            conn.rollback()
            msg = "error in operation
            
        finally:
            return render_template('addrec.html', msg=msg)
            conn.close()
            
  if __name__ = '__main__'
  
  #tdebug=true allows you to see changes in the coding environment
  #without running the server again.
  app.run(debug = true)
            
 
        

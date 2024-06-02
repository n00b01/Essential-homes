from flask import Flask, render_template, redirect, request, url_for, session
import pymysql
import os
from sms import send_sms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'beverly@123'



@app.route('/index')
def index():
     sql1= "SELECT *FROM homes "
     connection = pymysql.connect(host='localhost',user='root' , password='' ,database='essentialhome')
     cursor=connection.cursor()
     cursor.execute(sql1)
     homes= cursor.fetchall()
     connection = pymysql.connect(host='localhost',user='root' , password='' ,database='essentialhome' )
     cursor=connection.cursor()
     cursor.execute(sql1)
     homes= cursor.fetchall()
     return render_template('index.html' , homes=homes)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
@app.route('/feedback' ,methods =['POST' ,'GET'])
def feedback():
     
     if request.method =='POST':
          username=session.get('key')
          feedback=request.form['feedback']
          
           
          #connecting sql database
          connection = pymysql.connect(host='localhost' , user='root' ,password='' , database='essentialhome')
          sql='''INSERT INTO feedback (username, feedback) VALUES(%s,%s)'''
               
          cursor =connection.cursor()
          cursor.execute(sql,(username,feedback))
          connection.commit()
         
          return render_template('feedback.html' , success='Feedback uploaded Successfully')
     else:
          return render_template('feedback.html')
          
@app.route('/testimonial')
def testimonial():
     sql1= "SELECT * FROM feedback "
     connection = pymysql.connect(host='localhost',user='root' , password='' ,database='essentialhome')
     cursor=connection.cursor()
     cursor.execute(sql1)
     feedback= cursor.fetchall()
     connection = pymysql.connect(host='localhost',user='root' , password='' ,database='essentialhome' )
     return render_template('testimonial.html' , feedback=feedback)
@app.route('/register' ,methods =['POST' ,'GET'])
def register():
      if request.method =='POST':
          username=request.form['username']
          email=request.form['email']
          phone=request.form['phone']
          password1=request.form['password1']
          password2=request.form['password2']
          #password validation
          if len(password1) < 8:
               return render_template('register.html' , error='Password must be more than 8 characters')
          elif password1 !=password2:
               return render_template('register.html' , error='Password do not match')
          else:
           
          #connecting sql database
               connection = pymysql.connect(host='localhost' , user='root' ,password='' , database='essentialhome')
               sql='''INSERT INTO users (username, password, email, phone ) VALUES(%s,%s,%s,%s)'''
               
               cursor =connection.cursor()
               cursor.execute(sql,(username,password1,email,phone))
               connection.commit()
               #sending sms
               import sms
               send_sms(phone,"Thank you for registering with us")
               return render_template('login.html' , success='Registered Successfully')
      else:
          return render_template('register.html')
@app.route('/login' , methods= ['POST' ,'GET'])
def login():
     if request.method =='POST':
          username=request.form['username']
          password=request.form['password']
          #connecting sql
          connection =pymysql.connect(host='localhost' ,user='root' ,password='' ,database='essentialhome')
          sql ='''select * from users where username =%s and password =%s'''
          cursor= connection.cursor()
          cursor.execute(sql,(username,password))
          #
          if cursor.rowcount==0:
               return render_template('login.html' ,error ='Invalid Credentials')
          else:
               session['key']=username
               return redirect('/index')
     else:
          return render_template('login.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
     
@app.route('/propertylist')
def propertylist():
    return render_template('propertylist.html')
@app.route('/propertyagent')
def propertyagent():
    return render_template('propertyagent.html')
@app.route('/propertytype')
def propertytype():
    return render_template('propertytype.html')






@app.route('/moreproperty')
def moreproperty():
     sql1= "SELECT *FROM homes "
     connection = pymysql.connect(host='localhost',user='root' , password='' ,database='essentialhome')
     cursor=connection.cursor()
     cursor.execute(sql1)
     homes= cursor.fetchall()
     connection = pymysql.connect(host='localhost',user='root' , password='' ,database='essentialhome' )
     cursor=connection.cursor()
     cursor.execute(sql1)
     homes= cursor.fetchall()
     return render_template('moreproperty.html' , homes=homes)
 

    


#upload property
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        try:
            property_category = request.form['property_category']
            property_type = request.form['property_type']
            property_cost = request.form['property_cost']
            property_name = request.form['property_name']
            location = request.form['location']
            height = request.form['height']
            beds = request.form['beds']
            baths = request.form['baths']
            property_image_name = request.files['property_image_name']
            
            # Save the uploaded file to a specific directory
            image_path = 'static/img/' + property_image_name.filename
            property_image_name.save(image_path)

            # Connect to the MySQL database
            connection = pymysql.connect(
                host='localhost', user='root', password='', database='essentialhome', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            with connection.cursor() as cursor:
                # Execute the SQL query
                sql = "INSERT INTO homes (property_category, property_type, property_cost, property_name, location, height, beds, baths, property_image_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (property_category, property_type, property_cost, property_name, location, height, beds, baths, image_path))
                connection.commit()

            return render_template('upload.html', message='Property Added Successfully')
        except Exception as e:
            # If an error occurs, rollback the transaction and display an error message
            print("Error:", e)
            connection.rollback()
            return render_template('upload.html', message='Failed to add property. Please try again.')
        finally:
            connection.close()
    else:
        return render_template('upload.html', message='Please Add Property Details')

 #
@app.route('/bookings/<property_id>')
def bookings(property_id):
     connection =pymysql.connect(host='localhost', user='root' , password='', database='essentialhome')
     sql = "SELECT * FROM homes WHERE property_id= %s "
     cursor = connection.cursor()
     cursor.execute(sql , (property_id))
     if cursor.rowcount==0:
          return render_template('booking.html', message= 'Item Not Found')
     else:
          property= cursor.fetchone()
          return render_template('booking.html' , property=property)
@app.route('/booking' ,methods =['POST' ,'GET'])
def booking():
     
     if request.method =='POST':
          username=session.get('key')
          property_name=request.form['property_name']
          
           
          #connecting sql database
          connection = pymysql.connect(host='localhost' , user='root' ,password='' , database='essentialhome')
          sql='''INSERT INTO booking (username, feedback) VALUES(%s,%s)'''
               
          cursor =connection.cursor()
          cursor.execute(sql,(username,property_name))
          connection.commit()
         
          return render_template('booking.html' , success='Bookings uploaded Successfully')
     else:
          return render_template('booking.html')
     


if __name__ == '__main__':
    app.run(debug=True)

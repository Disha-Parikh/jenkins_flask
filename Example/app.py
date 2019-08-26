from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from User.model import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pineapple123@localhost:15432/postgres'
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
db.session.commit()
@app.route('/data',methods=["GET","POST"])
def index():
	if(request.method == "POST"):
		id = request.form['id']
		name= request.form['name']
		email = request.form['email']
		status = request.form['status']
		user = User(id=id,user_name=name,user_email=email,status=status)
		db.session.add(user)
		db.session.commit()
	return render_template('index.html')
if __name__ == '__main__':
    app.run()

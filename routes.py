from flask import render_template , url_for , flash , redirect , request , jsonify , json 
from ProiectPa import app , db 
from flask_admin.contrib.sqla import ModelView
from ProiectPa.models import Post
from functools import wraps
from flask_login import login_user, current_user, logout_user, login_required




@app.route('/home')

def adtest():
   
    return render_template('layout.html')

@app.route('/order' , methods=['POST'])
def PostOrder():
    details = request.json['details']
    price = request.json['price']
    table = request.json['table']
    user_id=request.json['user_id']
    over=request.json['over']
    new_post = Post(details,price,table,user_id,over)
    db.session.add(new_post)
    db.session.commit()

@app.route('/orders' , methods=['GET'])
def GetOrders():
    details = request.json['details']
    price = request.json['price']
    table = request.json['table']
    user_id=request.json['user_id']
    over=request.json['over']
    new_post = Post(details,price,table,user_id,over)
    db.session.add(new_post)
    db.session.commit()

@app.route('/orderupd/<id>' , methods=['PUT'])
def UpdateOrder():
    post = Post.query.get(id)
    details = request.json['details']
    price = request.json['price']
    table = request.json['table']
    user_id=request.json['user_id']
    staff_id=request.json['staff_id']
    over=request.json['over']
    new_post = Post(details,price,table,user_id,staff_id,over)
    db.session.add(new_post)
    db.session.commit()
   
    


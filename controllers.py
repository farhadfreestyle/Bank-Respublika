from app import app
from models import *
from flask import render_template, request
from forms import *
import random
from api import *


@app.route("/campaign")
def campage():
    data = Campaign.query.all()
    return render_template('campaign.html', data = data)


@app.route("/card")
def card():
    data = Card.query.all()
    ids = []
    for i in data:
        ids.append(i.id)
    ids.sort()
    return render_template('cards.html', ids = ids, data = data)


@app.route("/order1", methods = ['GET', 'POST'])
def order1():   
    all_cards = Card.query.all()
    post_data = request.form
    print(post_data)
    global form1
    form1 = Order1()
    
    if request.method == 'POST':
        form1 = Order1(data= post_data)
        print(form1.validate_on_submit())
      
    
    return render_template('card-order1.html', form1 = form1, all_cards = all_cards)


@app.route("/order2", methods = ['GET', 'POST'])
def order2():
    data = Security_image.query.all()
    ids = [1, 2, 3]
    a = random.choice(ids)
    for i in data:
        if i.id == a:
            robot_image = i.image_url

    post_data = request.form
    print(post_data)
    global form2
    form2 = Order2()
    if request.method == 'POST':
        form2 = Order2(data= post_data)
        print(form2.validate_on_submit())
       

  
    return render_template('card-order2.html', form2 = form2, robot_image = robot_image)

@app.route("/order3",methods = ['GET', 'POST'])
def order3():
    form3 = Order3()
    if request.method =='POST':
        if form1.validate_on_submit() and form2.validate_on_submit():
            details = Card_user(order=form1.card.data, currency=form1.currency.data, time=form1.time.data, preparation=form1.preparation.data, sms=form1.sms.data, card_take=form1.card_take.data, branch=form1.branch.data, amount=form1.amount.data, location=form1.location.data, name=form2.name.data, surname=form2.surname.data, father=form2.father.data, unique_code=form2.unique_code.data, secret=form2.secret.data, phone = form2.phone.data, phone_extra=form2.phone_continue.data, mail=form2.email.data)
            details.save()
    return render_template('card-order3.html', form3 = form3)


@app.route("/currency")
def valyuta():
    return render_template('currency.html', dollar = dollar, euro = euro, ruble = ruble, gbp = gbp)



@app.route("/card<int:kart_index>")
def kart(kart_index):
    data = Card.query.all()
    ids = []
    for i in data:
        ids.append(i.id)
    
    return render_template('card.html',ids = ids, data = data, kart_index = kart_index)


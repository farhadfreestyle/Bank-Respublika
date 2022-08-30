
from app import app
from extensions import *


class Card(db.Model):
    id = db.Column(db.Integer(), unique = True ,autoincrement=True, nullable = False)
    ad = db.Column(db.String(100),nullable = False, primary_key = True)   
    description = db.Column(db.String(1000))
    haqq = db.Column(db.String(40))
    muddet = db.Column(db.String(20))
    image_url = db.Column(db.String(1000))
    qaliq = db.Column(db.String(40))    
    valyuta = db.Column(db.String(40))
    kredit = db.Column(db.String(40))



    def __repr__(self):
        return self.ad
    
    def __init__(self, id, ad, description, haqq, image_url, muddet, qaliq, valyuta, kredit):
        self.id = id
        self.ad = ad
        self.description = description
        self.haqq = haqq
        self.image_url = image_url
        self.muddet = muddet
        self.qaliq = qaliq
        self.valyuta = valyuta
        self.kredit = kredit


    def save(self):
        db.session.add(self)
        db.session.commit()





class Card_user(db.Model):
    
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    order = db.Column(db.String(40))
    currency = db.Column(db.String(40))
    time = db.Column(db.String(40))
    preparation = db.Column(db.String(40))
    sms = db.Column(db.String(40))
    card_take = db.Column(db.String(40))
    branch = db.Column(db.String(40))
    amount = db.Column(db.String(40))
    location = db.Column(db.String(40))
    name = db.Column(db.String(100))   
    surname = db.Column(db.String(40))
    father = db.Column(db.String(40))
    unique_code = db.Column(db.String(40))
    secret = db.Column(db.String(40))
    phone = db.Column(db.String(40))    
    phone_extra = db.Column(db.String(40))
    mail = db.Column(db.String(40))
    



    def __repr__(self):
        return self.ad
    
    def __init__(self, order, currency, time, preparation, sms, card_take, branch, amount, location, name, surname, father,unique_code,secret, phone, phone_extra, mail):
        self.order = order
        self.currency = currency
        self.time = time
        self.preparation = preparation
        self.sms = sms
        self.card_take = card_take
        self.branch = branch
        self.amount = amount
        self.location = location
        self.name = name
        self.surname = surname
        self.father = father
        self.unique_code = unique_code
        self.secret = secret
        self.phone = phone
        self.phone_extra = phone_extra
        self.mail = mail
    
      

    def save(self):
        db.session.add(self)
        db.session.commit()


class Campaign(db.Model):
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    image_url = db.Column(db.String(500))
    text = db.Column(db.String(200))   
    bold = db.Column(db.String(200))
    alt = db.Column(db.String(200))
  
    



    def __repr__(self):
        return self.ad
    
    def __init__(self, text, bold, alt, image_url):
        self.image_url = image_url
        self.text = text
        self.bold = bold
        self.alt = alt
      

    def save(self):
        db.session.add(self)
        db.session.commit()



class Security_image(db.Model):
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    image_url = db.Column(db.String(500))

    def __repr__(self):
        return self.ad
    
    def __init__(self,image_url):
        self.image_url = image_url
    
    def save(self):
        db.session.add(self)
        db.session.commit()

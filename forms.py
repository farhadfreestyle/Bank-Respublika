from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, Length, ValidationError


class Order1(FlaskForm):
    card = SelectField(label='Kartı əlavə et' ,choices=['Plastik kartın növünü seçin','NeoKart Premium', 'NeoKart Standard', 'MasterCard Wblack Edition PP', 'MasterCard World Elite', 'Visa Infinite', 'MasterCard Platinum', 'MC Platinum ADR100', 'Visa Platinum', 'MasterCard Gold World', 'Visa Platinum Mover', 'Visa Classic', 'MasterCard Standard', 'MasterCard Stickers', 'Debit MasterCard', 'Visa Rewards Mover', 'Visa Classic Vector'], validators=[DataRequired()])
    currency = SelectField(label='Kartın valyutasını seç', choices=['Kartın valyutasını seç','AZN', 'USD', 'EUR'], validators=[DataRequired()])
    time = SelectField(label='Kartın müddəti', choices=['Müddəti seçin','1 il - 90 AZN', '2 il - 180 AZN', '3 il - 270 AZN'], validators=[DataRequired()])
    preparation = SelectField(label='Kartın hazırlama müddətini seçin', choices=['1 gün - 10 AZN', '3 gün - 0 AZN'], validators=[DataRequired()])
    sms = BooleanField(label='SMS xəbərdarlıq (0.99 AZN aylıq)', default = "unchecked")   
    card_take = SelectField(label='Kartı necə əldə etmək istəyirsiz?', choices=['Filialdan', 'Kuryerlə'], validators=[DataRequired()])
    branch = SelectField(choices=['Filialı seçin','Xırdalan" filialı', '"Şəki" filialı', '“İnşaatçılar” şöbəsi', '“Sumqayıt” filialı', '"Tovuz" filialı', '"Gəncə" filialı', '"Mingəçevir" filialı', '"Yevlax" filialı', '“Bərdə” filialı', '"Zaqatala" filialı', '“Şirvan” filialı', '"Sabirabad" filialı', '"Quba" filialı', '“Qax” filialı', '"Masallı" fililalı', '"Lənkəran" filialı', '"Abşeron" şöbəsi', '"Xaçmaz" filialı', 'Baş Ofis'], validators=[DataRequired()])
    amount = SelectField(label='Kartın buraxılma haqqı', choices=['Kartın pulunu ödəməklə', 'İlkin Mədaxil ödəməklə'], validators=[DataRequired()])
    location = StringField(label="Ünvanı daxil edin")


class Order2(FlaskForm):
    name = StringField(label="Tam adı daxil edin", validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    father = StringField(validators=[DataRequired()])
    unique_code = StringField(label = 'FİN kodunuz',validators=[DataRequired()], render_kw={'placeholder':"- - - - - - -"})
    secret = StringField(label="Məxfi söz", render_kw={'placeholder':"Məxfi sözü daxil edin"}, validators=[DataRequired()])
    phone = SelectField(label='Mobil nömrəniz',choices=['50', '51', '55', '10', '99', '70', '77'], validators=[DataRequired()])
    phone_continue = IntegerField(validators=[DataRequired()])
    email = EmailField(label="E-mail ünvanınız", validators=[DataRequired()])
    asan = BooleanField(label='Asan Finance-dan şəxsi məlumatlarımın istifadəsinə razılıq verirəm', default = "unchecked")
    robot_code = StringField(render_kw={'placeholder':'Kodu daxil edin'}, validators=[DataRequired()]) 



class Order3(FlaskForm):
    code = StringField(label="Kodu əlavə edin", validators=[DataRequired()])
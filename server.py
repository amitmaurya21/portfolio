from flask import Flask, render_template, url_for, request,redirect
import csv
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sonuu021@gmail.com'
app.config['MAIL_PASSWORD'] = 'ouvkgfhvldfqlozm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/submit_form', methods= ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return render_template('thank_you.html')

        except:
            return 'Did not save to database!'
    else:
        return 'Form submit error! Please try again.'

@app.route('/index.html')
def home_logo():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database:
        name = data['Name']
        email = data['Email']
        subject = data['Subject']
        message = data['Message']

        file = csv.writer(database, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file.writerow([name,email,subject,message])
        msg = Message(
            'Hello',
            sender='sonuu021@gmail.com',
            recipients=['sonuu021@gmail.com']
        )
        mail = Mail(app)
        msg.body = f'Sender name:{name}\nSender email address:{email}\nMail subject:{subject}\nMessage:{message}'
        print(msg)
        mail.send(msg)
    return 'Sent'


if __name__ == '__main__':
    app.run(debug=True)


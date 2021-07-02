from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)


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
        #fieldnames = ['Name', 'Email','Subject','Message']
        #writer = csv.DictWriter(database, fieldnames=fieldnames)

        #writer.writeheader()
        file = csv.writer(database, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file.writerow([name,email,subject,message])




if __name__ == '__main__':
    app.run(debug=True)


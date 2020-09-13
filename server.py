from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_info', methods=['POST', 'GET'])
def submit_info():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'didnot save to database'
    else:
        return 'something went wrong, Try again'


def write_to_file(data):
    with open('database.txt', 'a') as myfile:
        email = str(data.get('email'))
        subject = str(data.get('subject'))
        message = str(data.get('message'))
        myfile.write(f'{email},{subject},{message} \n')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as myfile2:
        email = str(data.get('email'))
        subject = str(data.get('subject'))
        message = str(data.get('message'))
        csv_writer = csv.writer(myfile2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])





from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.template_filter('format_date')
def format_date(value, format="%Y-%m-%d"):
    return value.strftime(format)

@app.route('/portfolio')
def portfolio():
    date_string = "2024-10-01"  
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    return render_template('portfolio.html', date=date_object)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)

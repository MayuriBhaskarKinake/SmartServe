from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/provider')
def provider():
    return render_template('provider.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

#object creation
app = Flask(__name__)

# Creating routes in our webapp
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    data = [{'name' : 'Shawshank Redemption', 'rating' : 9.2}, {'name' : 'Batman dark knight', 'rating' : 8.7}]
    return render_template('home.html', data = data)

if __name__ == "__main__":
    app.run(debug = True)
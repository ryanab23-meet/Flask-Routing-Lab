from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def home():
    products = ["Milk,egg,bread,meat,"]
    return render_template(
    "home.html",products="products")

@app.route('/milk')
def milk():
    return render_template('milk.html')

@app.route('/egg')
def egg():
    return render_template('egg.html')

@app.route('/bread')
def bread():
    return render_template('bread.html')

@app.route('/meat')
def meat():
    return render_template('meat.html')    
#Your code should be above 
 
if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)

from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')  

@app.route('/homepage')
def  homepage():    
     return render_template("homepage.html")

@app.route('/shoppingdirectory')
def  shoppingdirectory():    
     return render_template("shoppingdirectory.html")

@app.route('/orderpage')
def orderpage():
      return render_template("orderpage.html")

@app.route('/checkout')
def checkout():
      return render_template("checkout.html")

@app.route('/collection')
def collection():
      return render_template("collection.html")

@app.route('/delivery')
def delivery():
      return render_template("delivery.html")

@app.route('/qrcode')
def qrcode():
      return render_template("qrcode.html")

@app.route('/selfpickup')
def selfpickup():
      return render_template("selfpickup.html")

@app.route('/shoppingcart')
def shoppingcart():
      return render_template("shoppingcart.html")

@app.route('/paymentmade')
def paymentmade():
      return render_template("paymentmade.html")

if __name__=="__main__":
       app.run(debug=True,host='0.0.0.0')
# put the liberies 
from flask import Flask, render_template,request


# connect the html file and css files 
app = Flask(__name__,static_folder='statics', template_folder='Template')

# homes connect the flask 
@app.route("/")
def home():
    return render_template("index.html")

# connect the button 
@app.route("/submit",methods=["POST"])
def submit():
    #html form data
    Your_Name  = request.form['Your Name']
    Email_Address = request.form["Email Address"]
    Subject = request.form['Subject']

    # Show on the pages
    print(Your_Name)
    print(Email_Address)
    print(Subject)

    return "Form submit successful"


if __name__ == "__main__":
    app.run(debug=True)
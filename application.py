"""
Flask - class that represents Flask application, can create an instance to run web app
request - object that encapsulates the details of an HTTP request sent by the client
render_template - function that allows rendering of HTML templates 
"""
from flask import Flask, request, render_template  # importing modules
import passgen  # importing the password generation code already written

application = Flask(__name__)  # Flask constructor


@application.route(
    "/", methods=["GET", "POST"]
)  # decorator used to define a route for a specific URL pattern (root) and specify the HTTP methods that are allowed for that route (both "GET" and "POST")
def passlen():
    if request.method == "POST":  # checks if current HTTP request is POST
        password_length = int(
            request.form.get("pwdlen")
        )  # retrieves values from the fields of the form by their own name that were submitted via a POST request
        password_quantity = int(request.form.get("pwdquant"))
        res = passgen.generatepwd2(password_length, password_quantity)
        return render_template("out.html", passwd=res)
    return render_template(
        "index.html"
    )  # to display the content on the rendered HTML page


if __name__ == "__main__":  # to check if current script is main module
    application.run()  # starts the Flask development server

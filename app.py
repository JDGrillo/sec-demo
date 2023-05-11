# create an function that takes in the user's name and job title, and prints out a customized greeting based on their job
def greeting(name, job):
    # print("Hello " + name + ", you are a " + job)
    # update the print statement to be more insteresting of a reponse, using a dictionary to translate the job title into a more interesting word
    job_dict = {
        "programmer": "coding master",
        "engineer": "builder of things",
        "scientist": "mad scientist",
        "doctor": "healer of the sick",
        "lawyer": "arguer of things"
    }
    if job in job_dict:
        return "Hello " + name + ", you are a " + job_dict[job]
    return "Hello " + name + ", you are a " + job + ", which is a very interesting job."

# create a web app that takes in a user's name and job title, and prints out a customized greeting based on their job
# import Flask
from flask import Flask, render_template, request

# create an instance of the Flask class
app = Flask(__name__)

# create a route decorator to tell Flask what URL should trigger our function
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greeting", methods=["POST"])
def greetings():
    # call the above greeting function, passing in the name and job title from the form submission in the greeting.html file
    # call the greeting function
    return render_template("greetings.html", greeting=greeting(request.form.get("name"), request.form.get("job")))

# run the app
if __name__ == "__main__":
    app.run(debug=True)

# create a greeting html page that renders the greeting
# Path: templates/greeting.html


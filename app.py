from flask import Flask, request, jsonify, render_template
import random
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# @app.route('/submit-quiz', methods=['POST'])
# def submit_quiz():
#     data = request.json
#     dining_halls = ['john jay', 'ferris', 'faculty house']
#     selected_hall = random.choice(dining_halls)
#     return jsonify({"diningHall": selected_hall})

@app.route("/")
def hello_world():
    #return app.send_static_file("index.html")
    #return "<p>hELLO,World!<p>"
    #return app.send_static_file("/Users/mariammustafa/Downloads/checkpoint4b/src/QuizPage.jsx")
    return render_template("Home.html")

@app.route('/submit-quiz', methods=['GET', 'POST'])
def submit_quiz():
    #return jsonify({"message": "Endpoint working"})
    #return app.send_static_file("QuizPage.jsx")
    data = request.json
     # Assuming you want to select a dining hall randomly
    dining_halls = ['john jay', 'ferris', 'faculty house']
    selected_hall = random.choice(dining_halls)
    return jsonify({"diningHall": selected_hall})
    #return jsonify(message="working")

@app.route('/quiz-page', methods=['GET', 'POST'])
def quiz_page():
    return render_template("QuizPage.html")

@app.route('/quiz-results', methods=['GET', 'POST'])
def quiz_results():
    # data = request.json
    #  # Assuming you want to select a dining hall randomly
    # dining_halls = ['john jay', 'ferris', 'faculty house']
    # selected_hall = random.choice(dining_halls)
    # jsonify({"diningHallName": selected_hall})
    #return render_template("QuizResults.html", diningHallName= selected_hall)
    return render_template("QuizResults.html")

@app.route('/submit-review', methods=['GET', 'POST'])
def submit_review():
    return render_template("submit-review.html")

@app.route('/dietary-restrictions', methods=['GET', 'POST'])
def dietary_restrictions():
    return render_template("dietaryRestrictions.html")

@app.route('/generate-results', methods=['GET', 'POST'])
def generate_results():
    return render_template("generate-results.html")

@app.route('/community-uploads', methods=['GET', 'POST'])
def uploads():
    return render_template("community-uploads.html")

@app.route('/imagesss', methods=['GET', 'POST'])
def images():
    return render_template("image.html")

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template("profile.html")

@app.route('/dininglocations', methods=['GET', 'POST'])
def diningLocations():
    return render_template("diningsLocations.html")

@app.route('/review-posted', methods=['GET', 'POST'])
def reviewposted():
    return render_template("review-posted.html")

### PSEUDOCODE FOR DINING HALL MATCHER ALGO
# def getOfferings():
#   #import CSV/open file and iterate thru rows/columns
#   dictionary with key/value pairs
#   dining halls = key, cuisine = value
#   offerings = {}
#   for row, col in CSV:
#       offerings.update(row : col)
# at this point, dictionary is complete
# now, get input from user
# if input in offerings.values():
#    return "offerings.key() " + "is serving" + input
#    else
#      return "no matches for" + input + "found"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

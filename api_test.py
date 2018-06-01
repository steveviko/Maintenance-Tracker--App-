from flask import Flask, render_template,url_for,request, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalog in the form of a list of dictionaries.
users = [
    {'id': 0,
     'User FirstName': 'Moses',
     'User LasnName': 'Verno',
     'profession': 'Engineer.',
     'Age': '39'},
    {'id': 1,
     'User FirstName': 'Mike',
     'User LasnName': 'koola',
     'profession': 'Software Developer.',
     'Age': '16'},
    {'id': 2,
     'User FirstName': 'Chris',
     'User LasnName': 'looki',
     'profession': 'Doctor.',
     'Age': '12'},
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/api/v1/project/tests/users/all', methods=['GET'])
def api_all():
    return jsonify(users)


@app.route('/api/v1/project/tests/users', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for user in users:
        if user['id'] == id:
            results.append(user)

    # Use the jsonify function from Flask to convert our list of
   
    return jsonify(results)

app.run()

if __name__ == '__main__':
    app.run(debug=True)
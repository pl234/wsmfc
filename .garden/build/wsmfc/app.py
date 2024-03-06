from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/display_json")
def display_json():
    # Read the JSON file
    with open('Test_ALL_results.json', 'r') as f:
        json_data = f.read()
    
    # Return the JSON data as a response
    return jsonify(json_data)

@app.route("/") 
def index(): 
    return "Cooking Json! Hold on!!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)

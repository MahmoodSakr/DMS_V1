from flask import Flask, request, jsonify, render_template
# import model function
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/data", methods=["POST"])
def data():
    prompt = request.json.get("prompt")
    history_case_title = request.json.get("history_case_title")
    history_case_actions = request.json.get("history_case_actions")
    system = request.json.get("system")
    category = request.json.get("category")
    return {
        "prompt": prompt,
        "system": system,
        "category": category,
        "history_case_title": history_case_title,
        "history_case_actions": history_case_actions,
    }
    #import Model function to receive these data 
    #get model answer and return to the frontend   
	#result = AI_Model_import(all_inputs)
    #responce_data = {"data":", result}
    return responce_data,200

port = 5000
if __name__ == "__main__":
    print("Running from module: ", __name__)
    print("Flask Server is running on port", port)
    app.run(port=port)
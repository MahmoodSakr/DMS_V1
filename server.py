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
    #import Model function to receive these data 
    # get model answer and return to the frontend   
    return {
        "prompt": prompt,
        "system": system,
        "category": category,
        "history_case_title": history_case_title,
        "history_case_actions": history_case_actions,
    }
#    responce_data = {"data":"Llama result", "Medi"}
    return responce_data,200

PORT = 4000
if __name__ == "__main__":
    print("__name__ : ", __name__)
    print("Flask Server is running on PORT", PORT)
    app.run(port=PORT, debug=True)
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def alert_msg():
    response_data = {
        "isToDisplay": True,
        "header": "header",
        "content": "This is content"
    }
    
    response_json = json.dumps(response_data)
    return response_json
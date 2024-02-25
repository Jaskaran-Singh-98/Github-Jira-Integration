from flask import Flask,request
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():


        url = "https://jirasetup5.atlassian.net/rest/api/3/issue"

        API_TOKEN="Put-Your-Jira-API-Token-Here"
        auth = HTTPBasicAuth("Put-Your-email-which-is-used-to-login-to-Jira", API_TOKEN)

        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        payload = json.dumps( {
        "fields": {

            "description": {
            "content": [
                {
                "content": [
                    {
                    "text": "My First Jira Ticket",
                    "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },
            "issuetype": {
            "id": "10001"
            },
            "project": {
            "key": "SCRUM4"
            },
            "summary": "First JIRA Ticket",
        },
        "update": {}
        } )


        webhook = request.get_json()

        required_output = webhook['comment']['body']

        if (required_output  == '/jira'):
            response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
            )

            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

        else:
             print("Jira issue will be created if comment include /jira")


if __name__ == '__main__':
  app.run('0.0.0.0', port=4567)

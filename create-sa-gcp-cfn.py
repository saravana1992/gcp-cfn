from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def create_iam(req):
    disp_name = req.form.get('disp-name')
    descrip = req.form.get('descrip')
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('iam', 'v1', credentials=credentials)
    # Required. The resource name of the project associated with the service
    # accounts, such as `projects/my-project-123`.
    name = 'projects/crafty-mile-241013'  # TODO: Update placeholder value.
    create_service_account_request_body = {
        "serviceAccount": {
            "displayName": disp_name,
            "description": descrip
        },
        "accountId": "crafty-mile-241013"
    }
    request = service.projects().serviceAccounts().create(name=name, body=create_service_account_request_body)
    response = request.execute()
    
    # TODO: Change code below to process the `response` dict:
    pprint(response)

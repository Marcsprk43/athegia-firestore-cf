import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pandas import Series
import datetime

import os

# Use the application default credentials
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred, {
  'projectId': 'athegiamedical',
})

db = firestore.client()


def save_fs_document(collection, path, results_dict):
    try: 
        tileRef = db.document('{}/{}'.format(collection, path))
        tileRef.set(results_dict)
        
        return True
    except Exception as e:
        print(e)        
        return '{}'.format(e)    

# set the firestore collection and path template
fs_collection = 'biometrics'
fs_path = '{}/results/{}'

################################################################################################################
################################################################################################################
################################################################################################################


def save_data(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    }

    request_json = request.get_json()
    if request.args and 'data' in request.args:
        query_dict = request.args.get('data')
    elif request_json and 'data' in request_json:
        query_dict = request_json['data']
    else:
        return f'Hello World!'

    patient_uuid = query_dict['patient_uuid']
    document_name = query_dict['timestamp']
    payload = query_dict['payload']

    res = save_fs_document(fs_collection, fs_path.format(patient_uuid, document_name), payload)

      
    return (res, 200, headers)
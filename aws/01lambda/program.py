import json
import numpy as np
import joblib
lr_pred = joblib.load('lr.pkl')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    key1 = float(body['key1'])
    key2 = float(body['key2'])
    key3 = float(body['key3'])
    key4 = float(body['key4'])
    key5 = float(body['key5'])
    key6 = float(body['key6'])

    list_values = [key1,key2,key3,key4,key5,key6]    
    print(list_values)
    array_values = np.array(list_values)
    pred = lr_pred.predict([array_values])
    pred[0]
            
    return {
        'statusCode': 200,
        'body': json.dumps('Respond: ' + str(pred[0]))
    }
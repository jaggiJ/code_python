# SERVER HEALTH STATUS LOGGER
# jaggiJ 2021

# Checks server response status periodically, logs each non '200'
# Responses that are '200' or server error are logged less frequently to prevent spam

import requests
import time, datetime

# appends server response status to log
def append_status():
    res_msg = f'{str(datetime.datetime.now())} status code: {code}\n'
    with open('server_health_log.txt', 'a') as file:
        file.write(res_msg)

def estimate_status():
    try:
        req = requests.get('https://wypas.online')
        
    except:
        req = 'server error'

    if isinstance(req, str):
        code = 'server error'
    else:
        code = req.status_code
    return req, code

# initial log entry
req, code = estimate_status()
append_status()
print(f'Initial status code {code}, request: {req}')

counter = 0
while True:
    counter += 1
    req, code = estimate_status()
    
    if code != 200:
        append_status() 
    elif isinstance(code, str):
        if counter % 2 == 0:
            append_status()
    else:
        if counter % 6 == 0:
            append_status()
    

    time.sleep(300)

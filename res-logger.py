# WEB-SERVER RESPONSE STATUS LOGGER
# MIT License
# Copyright (c) 2021 jaggiJ

# Checks and logs server response status 

# USE:  'python[3] res-logger.py <server-address> <request time seconds>'
#   for testing:
#       'python3 res-logger.py https://google.com 6'
#       'tail -F status.log'
#   example for permanent run in background:
#       'python3 res-logger.py https://google.com 300 &'

import requests, sys
import time, datetime

#######################################################################
# SERVER AND REQUESTS TIME CONFIGURATION
# COMMAND LINE ARGUMENTS, IF PROVIDED OVERWRITE THIS
# server = 'https://server.address.here.com'
# requestFrequency = 300
server = 'https://wypas.online'
requestFrequency = 6

########################################################################
#FUNCTIONS
def append_status():
    '''Appends server response status to log.'''
    timeNow = datetime.datetime.now()
    formatTimeNow = timeNow.strftime("%d/%m/%Y, %H:%M:%S")
    res_msg = f'{formatTimeNow} status code: {code}\n'
    with open('status.log', 'a') as file:
        file.write(res_msg)

def estimate_status():
    '''Figures out server response code e.g. 200.'''
    try:
        req = requests.get(server)
    except:
        req = 'no connection to server'

    if isinstance(req, str):
        code = 'no connection to server'
        # code = 201 #debug
    else:
        code = req.status_code
    return req, code

def help_text():
    '''Prints out help to user.'''
    print(
'Add one or two arguments:\n1. server address starting with http\
or https,\n2. time in seconds (default is 300), e.g\n"python3 \
res-logger.py https://google.com 6"')
    sys.exit()

##########################################################################
#COMMAND LINE ARGUMENTS
commandLineArgs = sys.argv[1::]
if commandLineArgs:
    #Checks if user provided proper command line arguments; if not 
    #prints out help.
    if commandLineArgs[0].startswith('http') and commandLineArgs[1]:
        server = commandLineArgs[0]
        requestFrequency = int(commandLineArgs[1])
    elif commandLineArgs[0].startswith('http') and commandLineArgs == 1:
        server = commandLineArgs[0]
    else:
        help_text()

elif not commandLineArgs and server == 'https://server.address.here.com':
    help_text()   

###############################################################################
#OTHER VARIABLES
req, code = estimate_status()
lessFrequent = 6

###############################################################
append_status()
print(f'Initial status code {code}, request: {req}')

#MAIN LOOP
counter = 0
while True:
    #Sends requests and logs responses to file.
    
    counter += 1
    previous_status = code
    req, code = estimate_status()
    
    if code != previous_status:
        append_status() 
    else:
        #Decrease frequency of logging same status by calm_factor       
        if counter % lessFrequent == 0:
            append_status()

    time.sleep(requestFrequency)

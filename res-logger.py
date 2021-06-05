# WEB-SERVER RESPONSE STATUS LOGGER
# MIT License
# Copyright (c) 2021 jaggiJ

# Checks server response status each 5min by default settings and
# logs response code into file. Normal response (200) and connection 
# problems are logged less frequently to prevent spam in log file

# example: 
#       default setting 300 will check server each 5 min and append 
#       result to log. Exceptions: '200' code result - each 30 min,
#       connection error - each 10 min.

# USE:  'python[3] SCRIPT-NAME [SERVER-ADDRESS] [REQUEST-TIME-IN-SECONDS]'
#   e.g.'python3 res-logger.py https://google.com 6'

import requests, sys
import time, datetime

#######################################################################
# SERVER AND REQUESTS TIME CONFIGURATION
# COMMAND LINE ARGUMENTS, IF PROVIDED OVERWRITE THIS
server = 'https://server.address.here.com'
requestFrequency = 300

########################################################################
#FUNCTIONS
def append_status():
    '''Appends server response status to log.'''
    res_msg = f'{str(datetime.datetime.now())} status code: {code}\n'
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

#########################################################################
#OTHER VARIABLES
req, code = estimate_status()
append_status()
print(f'Initial status code {code}, request: {req}')

###############################################################
#MAIN LOOP
counter = 0
while True:
    #Sends requests and logs responses to file.
    
    counter += 1
    req, code = estimate_status()
    
    if code != 200 and not isinstance(code, str):
#         print('1 is case') #debug
        append_status() 
    elif isinstance(code, str):
        #Decrease frequency of connection error log.
#         print('2 is case') #debug
        if counter % 2 == 0:
            append_status()
    else:
        #Decrease frequency of logging code status 200.
#         print('3 is case') #debug
        if counter % 6 == 0:
            append_status()

    time.sleep(requestFrequency)

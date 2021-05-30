### code_python 

 ###############################################################################################
### SERVER HEALTH STATUS LOGGER
Runs in background. Sends get request every 5 min to server and appends result to log file 'server_health_log.txt'.

USAGE:
$ python server_health.py &

SUGGESTED EDITs:
1. Change server address in 'def estimate_status():'
2. Change time of requests in seconds at 'time.sleep(300)'

################################################################################################
 

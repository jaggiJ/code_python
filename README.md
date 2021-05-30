### SERVER HEALTH STATUS LOGGER
Runs in background. Sends get request every 5 min to server and appends result to log file 'server_health_log.txt'.
<hr>

USAGE: <br>
$ python server_health.py & <br>
<hr>

EXIT: <br>
$ fg <br>
<code>ctrl + C <br></code>
<hr>

SUGGESTED EDITs: <br>
1. Change server address in 'def estimate_status():'
2. Change time of requests in seconds at 'time.sleep(300)' ( change to 6 for initial testing )
<hr>

EXAMPLE OF LOG FILE ENTRIES <br>
2021-05-30 18:35:38.196089 status code: 200 <br>
2021-05-30 18:37:30.038671 status code: 200 <br>
2021-05-30 18:39:42.655819 status code: server error <br>
################################################################################################
 

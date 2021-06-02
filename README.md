## WEB-SERVER RESPONSE STATUS LOGGER<br>
### jaggiJ 2021<br>
<hr>
Checks server response status each 5min by default settings and<br>
logs response code into file. Normal response (200) and connection <br>
problems are logged less frequently to prevent spam in log file<br>
<hr>
#Defaults: <br>
      default setting 300 will check server each 5 min and append <br>
      result to log,<br>
      '200' code result - log each 30 min.<br>
      connection error - log each 10 min.<br>
      any other code - log each 5 min.<br>
<hr>
#Execution:<br>
syntax 'python[3] SCRIPT-NAME [SERVER-ADDRESS] [REQUEST-TIME-IN-SECONDS]'<br>
testing <code>'python3 res-logger.py https://google.com 6'</code><br>
production <code>'python3 res-logger.py https://your-web-server.com 300 &'</code><br>
<hr>
## EXAMPLE OF LOG FILE ENTRIES FROM 'testing'<br><br>
2021-06-02 17:49:13.500584 status code: 201 <br>
2021-06-02 17:49:19.590591 status code: 201<br>
2021-06-02 17:49:25.683361 status code: 201<br>
2021-06-02 17:49:33.065966 status code: no connection to server<br>
2021-06-02 17:49:39.239499 status code: no connection to server<br>
2021-06-02 17:49:51.428528 status code: no connection to server<br>
2021-06-02 17:50:03.622152 status code: no connection to server<br>
2021-06-02 17:50:15.830541 status code: no connection to server<br>
2021-06-02 17:50:28.027409 status code: no connection to server<br>
2021-06-02 17:50:40.214422 status code: no connection to server<br>
2021-06-02 17:51:17.568278 status code: 200<br>
2021-06-02 17:51:54.717402 status code: 200<br>
################################################################################################
 

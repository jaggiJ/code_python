## WEB-SERVER RESPONSE STATUS LOGGER<br>
### jaggiJ 2021<br>
<hr>
Checks server response status each 5min by default and logs response<br>
code into file, except when its same. Then logs less frequently.<br>
<hr>
Dependency: requests<br>
<hr>
#Execution:<br>
syntax 'python[3] res-logger.py [server_address] [seconds]'<br>
testing: <br>
<code>'python3 res-logger.py https://web-address.com 6 &'</code><br>
<code>'tail -F status.log'</code><br>
typical run: <br>
<code>'python3 res-logger.py https://your-web-server.com 300 &'</code><br>
<hr>
## EXAMPLE OF LOG FILE<br><br>
2021-06-02 17:49:13 status code: 201 <br>
2021-06-02 17:49:19 status code: 201<br>
2021-06-02 17:49:25 status code: 201<br>
2021-06-02 17:49:33 status code: no connection to server<br>
2021-06-02 17:49:39 status code: no connection to server<br>
2021-06-02 17:49:51 status code: no connection to server<br>
2021-06-02 17:50:03 status code: no connection to server<br>
2021-06-02 17:50:15 status code: no connection to server<br>
2021-06-02 17:50:28 status code: no connection to server<br>
2021-06-02 17:50:40 status code: no connection to server<br>
2021-06-02 17:51:17 status code: 200<br>
2021-06-02 17:51:54 status code: 200<br>
################################################################################################
 

![](./logo.png)

```
HTTP/1.1 200 OK
Date: Mon, 30 Sep 2019 15:35:17 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Wed, 03 Jul 2019 22:47:23 GMT
ETag: "9a-58ccea50ba4c6-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Length: 154
Connection: close
Content-Type: text/html

<h1>This page is not ready yet !</h1>
<h2>We should redirect you to the required page !</h2>

<meta http-equiv="refresh" content="0; URL='/centreon'" />
```


http://10.10.10.157/centreon/api/index.php?action=authenticate


Running `brute.py` gives us the password `password1`.

```
Centreon 19.04  - Remote Code Execution                          | exploits/php/webapps/47069.py
```


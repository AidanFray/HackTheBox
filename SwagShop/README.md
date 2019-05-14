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

We need to become authenticated to run this exploit:

https://www.exploit-db.com/exploits/37811

Blog post

https://websec.wordpress.com/2014/12/08/magento-1-9-0-1-poi/
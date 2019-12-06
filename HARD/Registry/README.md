http://docker.registry.htb/v2/  Looks like a docker hub?

```
admin:admin
```


/etc/docker/daemon.json

```
{
  "insecure-registries" : ["myregistrydomain.com:5000"]
}
```


http://docker.registry.htb/v2/_catalog


sudo docker pull docker.registry.htb/bolt-image
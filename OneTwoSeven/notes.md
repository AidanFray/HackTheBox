![](./logo.png)

# USER

`http` endpoing found using `nmap`. Source code of the page contains:

```html
<!-- Only enable link if access from trusted networks admin/20190212 -->
<!-- Added localhost admin/20190214 -->
<li class="nav-item"><a id="adminlink" class="nav-link disabled" href="http://onetwoseven.htb:60080/">Admin</a></li>
```

I'm going to add domain to `/etc/hosts` file.

Lots of mention of localhost on the webpage. Like:

- The box name OneTwoSeven (127)
- `DoubleColonOne` IPv6 localhost (::1)

Using the page http://onetwoseven.htb/signup.php we can sign up and get `sftp` access.
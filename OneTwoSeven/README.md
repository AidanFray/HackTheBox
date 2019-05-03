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

We can upload files, but the website blocks access to any files with a `.php` extension.

I think it has something to do with uploading a .htaccess file, but it doesn't seem to be working






### Creating an Apache module

Start off by generating a template:

```
apxs -g -n apache_module
```

This will create the files we need. To test it I'll run:

```
apxs -c -i mod_apache_module.c
```
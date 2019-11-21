![](./logo.png)

`nmap` shows a set of open ports, looking around the website does not give us much.

However, performing an extended `nmap` gives us the port 6379 that is a `redis` store.

Running the command:

```
$ redis-cli -h 10.10.10.160 KEYS "*"

1) "crackit"
```

Then we want to `dump` it:

```
$ redis-cli -h 10.10.10.160 dump "crackit"

"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYFaQnxyy+ioXad/PMf2O6h6vkpqvzkf2VJvY9dcHLrOTanUP6RypBGzPCDdvX7dggsazLDIEwqUyaQFgM4co53IuGJMOeZ2zMfMFFE/yvuBExtuwH0ZSprVBSMng336gBQxmzizyrbmjfqF1lKOQ31vXJQIZds39+c3MpF8kNq7GUmIECipewu84i3W6W8A3M6Rr2UgZMKNC0DyNZAHzmHntCkABkRC/6y8fua9bhTLCy5YB70trP0zXQfdgLwdXaG9L0Gzv/NQy+JZDBC/J0CvJgljcWYdWpkFyEjH0Gr4MjbBxRNEVgKqh2su43pzsqcy1tdB2Am5X1D9d6xJbd redis@postman"
```

We have an `ssh` RSA public key.



ssh-keygen -f key.pub -e -m pem


Redis 4.x / 5.x - Unauthenticated Code Execution


https://github.com/LoRexxar/redis-rogue-server
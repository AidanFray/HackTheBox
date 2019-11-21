Starting Nmap 7.70 ( https://nmap.org ) at 2019-03-11 16:05 UTC
PORT    STATE SERVICE    REASON  VERSION
22/tcp  open  ssh        syn-ack OpenSSH 7.9 (protocol 2.0)
| ssh-hostkey: 
|   2048 07:ca:21:f4:e0:d2:c6:9e:a8:f7:61:df:d7:ef:b1:f4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDELKAfm1BpeFVd8VUIghLbckoqlQCnzX91NNnUhk64KvTzAM4ZTg0jtpKF+UTNudSrSdJqhGT1Kp0jaKcLw9D5FVEMeuY6MdHEh4AKlJp46FXBhje5kPrw7deMPUQbEcMI6vD8odocp+OL19hcyMea5rh8+5EL3phIc4+joqPo2EndJguLBukIu5wTH6GRr7GDYsgRsyaH48wryhpzn36jtDkyzHWcP3BN/2O6eOTSz+MK4diPHaV3OPHiO0HfCl4DCUu0YsujVIhwvgjlAaKzd/qG2BMhTOUp+D/EOBfKvG5dWWAYDZYOzsyBoh7hyAA7t5jnytfURUgomghq++YR
|   256 30:4b:25:47:17:84:af:60:e2:80:20:9d:fd:86:88:46 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGN93hhLLZzrxWUPp9V+sD4Tw7qelUF2d/djEWnvR4q6m59QhnKSqY6jARBEdzTM2U/+/3rlzDdQLEt9Ne6mOqw=
|   256 93:56:4a:ee:87:9d:f6:5b:f9:d9:25:a6:d8:e0:08:7e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJQUfasxFtYgFy6VwI9Xe4PcrQrfF5dRdWIS/k0SoFv9
80/tcp  open  http       syn-ack OpenBSD httpd
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: OpenBSD httpd
|_http-title: Fortune
443/tcp open  ssl/https? syn-ack
|_ssl-date: TLS randomness does not represent time

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 107.83 seconds

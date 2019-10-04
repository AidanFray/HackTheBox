# Illumination

```
A Junior Developer just switched to a new source control platform. Can you find the secret token? 
```

The folder provides us with a `bot.js` and `config.json`. With further inspection it can be seen that a `.git` repo
is available.

Using the beautiful tool [Git Extractor](https://github.com/internetwache/GitTools/tree/master/Extractor) we can get the version history of the 
repo

In commit 3 we can see that the developer accidently adds the security token:

```
{

	"token": "=",
	"prefix": "~",
	"lightNum": "1337",
	"username": "UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ==",
	"host": "127.0.0.1"

}
```

Decoding this from `base64` gives us the flag!

```
HTB{v3rsi0n_c0ntr0l_am_I_right?}
```


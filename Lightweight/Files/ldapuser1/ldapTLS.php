<?php
$username = 'ldapuser1';
$password = 'f3ca9d298a553da117442deeb6fa932d';

// This code uses the START_TLS command

$ldaphost = "ldap://lightweight.htb";
$ldapUsername  = "cn=$username";

$ds = ldap_connect($ldaphost);
$dn = "uid=ldapuser1,ou=People,dc=lightweight,dc=htb"; 

if(!ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3)){
    print "Could not set LDAPv3\r\n";
}
else if (!ldap_start_tls($ds)) {
    print "Could not start secure TLS connection";
}
else
 {
// now we need to bind to the ldap server
$bth = ldap_bind($ds, $dn, $password) or die("\r\nCould not connect to LDAP server\r\n");

echo "TLS connection established.";
}
?>

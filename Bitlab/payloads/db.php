<?php 
    $db_connection = pg_connect("host=localhost dbname=profiles user=profiles password=profiles"); 
    $result = pg_query($db_connection, "SELECT * FROM profiles");

    while ($row = pg_fetch_row($result)) {
        echo $row[0]." - ".$row[1]." - ".$row[2]."\n";
    }
?>
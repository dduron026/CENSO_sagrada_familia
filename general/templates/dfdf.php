<?php 

$serverName = "DESKTOP-SF88S2C"
$connectionInfo = array("Database"=>"moodle", "UID"=>"sa", "PWD"=>"moodle31");
$conn = sqlsrv_connect( $serverName, $connectionInfo);	

if( $conn ) {
	echo "CONECTED";

}else{
	echo "CONECTION FAILED";
	die(print_r(sqlsrv_errors(), true));
}

?>

[opcache]
opcache.enable = 1
opcache.memory_consumption = 128
opcache.max_accelerated_files = 4000
opcache.revalidate_freq = 60

; Required for Moodle
opcache.use_cwd = 1
opcache.validate_timestamps = 1
opcache.save_comments = 1
opcache.enable_file_override = 0
<?php

$host = "localhost";
$dbname = "login_db";
$username = "root";
$password = "";

$mysqli = new mysqli(hostname: $host,
username: $username,
password: $password,
database: $dbname);

if($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: ";
}

return $mysqli;

 ?>

<?php
$lat = $_POST["lat"];
$lng = $_POST["lng"];
$file = fopen("location.txt", "a");
fwrite($file, "$lat,$lng\n");
fclose($file);
echo "Location stored successfully.";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1024, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>DnTrack configuration</title>
</head>
<body>
    <h1>Add a custom DNS entry</h1>
    <?php
    if(file_put_contents("/var/www/html/conf/userDNS.txt", $_POST["ip"] . " " . $_POST["hostname"] . "\n", FILE_APPEND) == FALSE)
        echo "<p>This was not successful</p>";
    else
        echo "<p>This was successful</p>";

    echo $_POST["ip"];
    echo '<br/>';
    echo $_POST["hostname"];
    
    ?>
</body>
</html>

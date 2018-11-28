<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1024, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>DnTrack configuration</title>
</head>
<body style="background-color: #000000; color: #FFFFFF; text-align: center;">
    <h1>Add a custom DNS entry</h1>
    <?php
    if(file_put_contents("userDNS.txt", $_POST["ip"] . " " . $_POST["hostname"] . "\n", FILE_APPEND) == FALSE)
        echo "<div style='background-color: #AA3333; color: #440000; width: auto; border-radius: 1em; padding: 30px;'><b>This was not successful!</b></div>";
    else
        echo "<p style='background-color: #33AA33; color: #004400; width: auto; border-radius: 1em; padding: 30px;'><b>Succesfully added custom DNS entry</b></p>";

    echo '<br><br>' . $_POST["ip"];
    echo '<br/>';
    echo $_POST["hostname"];
    
    ?>
</body>
</html>

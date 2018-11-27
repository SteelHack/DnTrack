<a href="addUser.html"> Add custom entry</a>
<h1>Summary</h1>
<table>
<tr>
<th>IP address</th>
<th>Hostname</th>
</tr>
<?php
$txt_file    = file_get_contents('/etc/hosts');
$rows        = explode("\n", $txt_file);
array_shift($rows);

foreach($rows as $row => $data)
{
    if($data[0] !== '#')
    {
    echo '<tr>';
    //get row data
    $row_data = explode(' ', str_replace("	"," ",$data), 2);

    $info[$row]['ip'] = $row_data[0];
    $info[$row]['hostname'] = $row_data[1];

    //display data
    echo '<td>' . $info[$row]['ip'] . '</td>';
    echo '<td>' . $info[$row]['hostname'] . '</td>';

    echo '</tr>';
    }
}
?>
</table>

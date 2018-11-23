<head>
	<title>DnTrack configuration</title>
</head>
<body>
<?php
	echo "PHP loaded";

	$fileHandler = fopen("testFile.conf", 'a');
	echo "debug-after fopen";
	fwrite($fileHandler, "\ndata inserted from php script");
	echo "debug-after fwrite";
	fclose($fileHandler);
	echo "debug-after fclose";
?>
</body>

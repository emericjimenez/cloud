<?php
$url = "https://link.aws/";
$data = array(        
	"key1" => "2012.917",
	"key2" => "19.5",
	"key3" => "306.59470",
	"key4" => "9",
	"key5" => "24.98034",
	"key6" => "121.53951"
);
$options = array(
'http' => array(
            'header' => "Content-type: application/json\r\n",
            'method' => 'POST',
            'content' => json_encode($data),
           ),
        );

$context = stream_context_create($options);
$result = file_get_contents($url, false, $context);
if ($result === FALSE) {
    die('Error.');
}
$data = json_decode($result, true);
echo $data;
?>


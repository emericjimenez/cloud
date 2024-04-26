<?php
$url = "https://aws-link/";
$data = array(        
	"key1" => "2",
	"key2" => "0.595",
	"key3" => "0.475",
	"key4" => "0.150",
	"key5" => "0.9145",
	"key6" => "0.3755",
	"key7" => "0.2055",
	"key8" => "0.2500"
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
$jsonObject = json_decode($result);
$answer = $jsonObject->answer;
echo $answer;
?>


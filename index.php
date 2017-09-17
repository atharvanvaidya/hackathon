<html>
<body>
<?php
$output = shell_exec('python flipkartselenium.py');
echo '<p>'.$output.'</p>';
?>
<form method="post">
     <div>
     <input type="text" id="input-name" placeholder="Enter keyword" name="formName">
 <input type="submit" name="input" value="Send">
 </div>
 </form>
<?php
if(isset($_POST['input-name'])){
if($_POST['input']=='Send')
{
	$sen=$_POST['formName'];
	$cmd1=shell_exec($sen);
	sleep(5);
	echo '<p>Hello Again</p>';
	echo '<p>'.$cmd1.'</p>';
}
}

?> 
 
</body>
</html>


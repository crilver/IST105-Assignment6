<?php
    $a = escapeshellarg($_GET['a']);
    $b = escapeshellarg($_GET['b']);
    $c = escapeshellarg($_GET['c']);
    $d = escapeshellarg($_GET['d']);
    $e = escapeshellarg($_GET['e']);
    $command = escapeshellcmd("python3 data_management.py $a $b $c $d $e");
    $output = shell_exec($command);

    echo "<h1>Assignment 6:</h1>";
    echo "<h2>Python Script Result</h2>";
    echo "<div>$output</div>";
?>
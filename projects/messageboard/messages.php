<?php
    if (isset($_POST['logout'])) {
        setcookie ("username", null, time()+36000);
        $_COOKIE['username'] = null;
    }
    if (isset($_POST['username'])) {
        setcookie ('username', $_POST['username'], time()+36000);
        $_COOKIE['username']=$_POST['username'];
    }
?>
<html>
    <head>
        <title>PHP Message Board</title>
    </head>

    <body>
        <h1>Melsage Board</h1>
<?php
    if (!isset($_COOKIE['username'])) {
        echo "<form action='' method='post'>";
        echo "  Username:<input type='text' name='username'          />";
        echo "  <input type='submit' value='Login' />";
        echo "</form>";
    }
    else {
        echo "<p>you are logged in as ".$_COOKIE['username'];
        echo "<form action='' method='post'>";
        echo "  Message: <textarea name='message'></textarea>";
        echo "  Logout: <input type='checkbox' name='logout'         />";
        echo "           <input type='submit'   value='Post Message' />";
        echo "</form>";

        $messageboard_filename = "messages.txt";

        if (isset($_POST['message'])) {
            $file = fopen($messageboard_filename, "a"); #Open file in append mode
            fwrite($file, "<p>".$_COOKIE['username'].": ".$_POST['message']."</p>\n");
            fclose($file);
        }

        $file = fopen($messageboard_filename, "r"); #Open the file in read mode
        $text = fread($file, filesize($messageboard_filename));
        fclose($file);
        echo ($text);
    }
?>
    </body>
</html>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="POST" onsubmit="return validateForm()">
        <label for="name">userName:</label>
        <input type="text" id="name" name="name">
        <input name="Submit" type="submit" value="Submit">
    </form>
    <?php
    $hostname = 'localhost';
    $username = 'root';
    $password = '';
    $databasename = 'practise';
    $message = '';

    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['Submit'])) {
        try {
            $mysqli = new mysqli($hostname, $username,"", $databasename);

            if ($mysqli->connect_error) {
                die("Connection failed: " . $mysqli->connect_error);
            }

            $username = $mysqli->real_escape_string($_POST['name']);            
            $sql="SELECT passwords from another WHERE username='rahul' ";
            $result=$mysqli->query($sql);


            if ($row = $result->fetch_assoc())
            {
                echo $row["passwords"];
                $message = 'Submitted successfully!';
                // Echo JavaScript code to display an alert
                echo '<script>alert("'.$message.'");</script>';
            } 
            else 
            {
                $message = 'Error: ' . $mysqli->error;
                // Echo JavaScript code to display an alert
                echo '<script>alert("'. $message .'");</script>';
            }

        } catch (mysqli_sql_exception $e) 
        {
            $message = 'Could not connect: ' . $e->getMessage();
            // Echo JavaScript code to display an alert
            echo '<script>alert("'.$message.'");</script>';
        }
        catch (Exception $e) {
            $message = 'An error occurred: ' . $e->getMessage();
            // Echo JavaScript code to display an alert
            echo '<script>alert("' . $message . '");</script>';
        }
    }
    ?>
</body>
</html>

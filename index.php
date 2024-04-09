<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="POST" onsubmit="return validateForm()">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <label for="password">Password</label>
        <input type="" id="password" name="password">
        <input name="Submit" type="submit" value="Submit">
    </form>
    <script>
        function validateForm() {
            var name = document.getElementById("name").value;
            var password = document.getElementById("password").value;
            var nameRegex = /^[a-zA-Z\s]+$/;
            var passwordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[0-9]).{10,}$/;
            if (!nameRegex.test(name)) {
                document.getElementById("name").style.borderColor = "red"; // Corrected method name
                alert("Name should contain only letters and spaces");
                return false;
            }

            if (!passwordRegex.test(password)) {
                document.getElementById("password").style.borderColor = "red"; // Corrected method name
                return false;
            }

            return true;
        }
    </script>
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
            $password =$mysqli->real_escape_string( $_POST['password']);
            

            $sql = "INSERT INTO user_table VALUES ('$username', '$password')";

            if ($mysqli->query($sql) === TRUE)
            {
                $message = 'Submitted successfully!';
                // Echo JavaScript code to display an alert
                echo '<script>alert("'. $message .'");</script>';
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

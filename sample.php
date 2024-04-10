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
        <input type="text" id="name" name="name"><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br>
        <label for="gender">Gender:</label>
        <select id="gender" name="gender">
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select>
        <br>
        <input type="radio" id="radioMale" name="radioGender" value="male">
        <label for="radioMale">Male</label>
        <input type="radio" id="radioFemale" name="radioGender" value="female">
        <label for="radioFemale">Female</label>
        <br>
        <input type="checkbox" id="agree" name="agree">
        <label for="agree">I agree to the terms and conditions</label>
        <br>
        <input name="submit" type="submit" value="Submit">
    </form>
    <script>
        function validateForm() {
            var name = document.getElementById("name").value;
            var password = document.getElementById("password").value;
            var gender = document.getElementById("gender").value;
            var radioGender = document.querySelector('input[name="radioGender"]:checked');
            var agree = document.getElementById("agree").checked;
            //var emailRegex = /^[A-Z0-9a-z_\.]{2,}@[a-zA-z]{5,}\.[a-zA-z]{3,}$/;
            //var numberRegex = /^[0-9]{10}$/;
            var nameRegex = /^[A-Za-z0-9]{3,8}$/;
            var passwordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[0-9]).{10,}$/;
            var isValid = true;

            if (!nameRegex.test(name)) {
                document.getElementById("name").style.borderColor = "red";
                alert("Name should contain only letters and spaces");
                isValid = false;
            }

            if (!passwordRegex.test(password)) {
                document.getElementById("password").style.borderColor = "red";
                alert("Password should contain at least one uppercase letter, one special character, one digit, and be at least 10 characters long");
                isValid = false;
            }

            if (gender === "") {
                alert("Please select your gender");
                isValid = false;
            }

            if (!radioGender) {
                alert("Please select your gender");
                isValid = false;
            }

            if (!agree) {
                alert("Please agree to the terms and conditions");
                isValid = false;
            }

            return isValid;
        }
    </script>

    <?php
    $hostname = 'localhost';
    $username = 'root';
    $password = '';
    $databasename = 'practise';

    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['submit'])) {
        $message = '';

        try {
            $mysqli = new mysqli($hostname, $username, $password, $databasename);

            if ($mysqli->connect_error) {
                die("Connection failed: " . $mysqli->connect_error);
            }

            // Sanitize user inputs to prevent SQL injection
            $username = $mysqli->real_escape_string($_POST['name']);
            $password = $mysqli->real_escape_string($_POST['password']);
            $gender = $mysqli->real_escape_string($_POST['gender']);
            $radioGender = $mysqli->real_escape_string($_POST['radioGender']);

            $sql = "INSERT INTO another (username, passwords, gender, role) VALUES ('$username', '$password', '$gender', '$radioGender')";

            if ($mysqli->query($sql) === TRUE) {
                $message = 'Submitted successfully!';
                echo '<script>alert("' . $message . '");</script>';
            } else {
                $message = 'Error: ' . $mysqli->error;
                echo '<script>alert("' . $message . '");</script>';
            }

        } catch (mysqli_sql_exception $e) {
            $message = 'Could not connect: ' . $e->getMessage();
            echo '<script>alert("' . $message . '");</script>';
        }
        catch (Exception $e) {
            $message = 'An error occurred: ' . $e->getMessage();
            echo '<script>alert("' . $message . '");</script>';
        }
    }
    ?>
</body>
</html>

<?php
//include "connexion_bd.php"

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $nom = $_POST["nom"];
    $prenom = $_POST["prenom"];
    $matricule = $_POST["matricule"];
    $password = $_POST["password"];

    

    // Validate and save data (in a real-world scenario, you would hash the password)
    if (!empty($matricule) && !empty($password)) {
        // Save data to a file (for simplicity, you might use a database in a real application)
        $user = 'root';
        $pass = '';
        $dbh = new PDO('mysql:host=localhost;dbname=car_renting',$user,$pass);
		$statement = $dbh->query("SELECT *FROM utilisateur");
		//$row = $statement->fetch(PDO::FETCH_ASSOC);
        foreach ($statement as $line)
            {
                
               if ($matricule == $line['matricule'] && $password == $line['password'])
               {
                header('Location: ../activities/index.html');
               }else {
               
                header('Location: ../index2.html');
               }
            }
        
        //file_put_contents("user_data.txt", $data, FILE_APPEND);
        // header('Location: ../home.html');

    } else {
        echo "Please fill in both username and password.";
    }
}
?>

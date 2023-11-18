<?php

session_start();

if (isset($_SESSION["user_id"])) {

    $mysqli = require __DIR__ . "/database.php";

    $sql = "SELECT * FROM user
            WHERE id = {$_SESSION["user_id"]}";

    $result = $mysqli->query($sql);

    $user = $result->fetch_assoc();
}
?>




<!DOCTYPE html>
<html>
<head>
    <title>Home</title>

</head>
<body>

    <h1>Home</h1>

    <?php if (isset($user)): ?>

        <p>Hello <?= htmlspecialchars($user["name"]) ?></p>

        <p><a href="logout.php">Log out</a></p>

    <?php else: ?>

        <p><a href="login.php">Log in</a> or <a href="signup.html">sign up</a></p>

    <?php endif; ?>

    <h1>List of Game Reviews</h1>

    <?php
    include("developers.php");
    ?>

        <?php echo $deleteMsg??''; ?>
          <table border="1">
           <thead><tr>
           <th>S.N</th>
           <th>Name</th>
           <th>Author</th>
           <th>Mark</th>
           <th>Url</th>
           <th>Platform/s</th>
        </thead>
        <tbody>
      <?php
          if(is_array($fetchData)){
          $sn=1;
          foreach($fetchData as $data){
        ?>
          <tr>
            <td><?php echo $sn; ?></td>
            <td><?php echo $data['name']??''; ?></td>
            <td><?php echo $data['author']??''; ?></td>
            <td><?php echo $data['mark']??''; ?></td>
            <td><?php echo $data['url']??''; ?></td>
            <td><?php echo $data['platform']??''; ?></td>
         </tr>
         <?php
          $sn++;}}else{ ?>
          <tr>
            <td colspan="8">
        <?php echo $fetchData; ?>
      </td>
        <tr>
        <?php
        }?>
        </tbody>
         </table>
</html>


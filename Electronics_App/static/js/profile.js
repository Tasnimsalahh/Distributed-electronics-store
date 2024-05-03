var userTable = document.getElementById('userTable');
var username = document.getElementById('username');
var firstname = document.getElementById('firstname');
var lastname = document.getElementById('lastname');
var email = document.getElementById('email');
var user = null;
async function getuser(){
    var response = await fetch(`http://127.0.0.1:8000/API/profile/?format=json`);
    var finalResponse = await response.json();
    console.log(finalResponse.username);
    user = finalResponse;
    displayUser();
}
getuser();
 
function displayUser(){
    username.innerHTML=user.username;
    firstname.innerHTML=user.first_name;
    lastname.innerHTML=user.last_name;
    email.innerHTML=user.email;
}
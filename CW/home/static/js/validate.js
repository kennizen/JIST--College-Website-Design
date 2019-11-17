function validate(){
    var username = document.getElementById('uname');
    var password = document.getElementById('pass');
   

    if(username.value == '' || password.value == '')
    {
        alert('Fields cannot be empty!');
        return false;
    }
    else 
    {
        return true;
    }      

}
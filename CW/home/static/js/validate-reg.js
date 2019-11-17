function validate(){
    var username = document.getElementById('uname');
    var password = document.getElementById('pass');
    var con_password = document.getElementById('cpass');


    var uname_value = username.value;
    var uname_length = uname_value.length;

    var pass_value = password.value;
    var pass_length = pass_value.length;



    if(username.value.trim() == '' || password.value.trim() == '')
    {
        alert('Fields cannot be empty !');
        return false;
    }
    else if(password.value.trim() != con_password.value.trim())
    {
        alert("Password doesn't match !");
        return false;
    }
    else if(uname_length < 3 )
    {
        alert('Username should be atleast three(3) characters long !');
        return false;
    }
    else if(pass_length < 4)
    {
        alert('Password should be atleast four(4) characters long !');
        return false;
    }
    else
    {
        return true;
    }

    

}
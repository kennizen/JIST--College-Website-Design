function validate(){
    var phone = document.getElementById('phone');
    var roll = document.getElementById('roll');
    var fname = document.getElementById('fname');
    var lname = document.getElementById('lname');
    var gname = document.getElementById('gname');
    var nl = document.getElementById('nl');
    var add = document.getElementById('add');


    var phone_value = phone.value;
    var phone_length = phone_value.length;
       

    var roll_value = roll.value;
    var roll_length = roll_value.length;

    if(phone_length < 10 || phone_length > 10)
    {
        alert('Invalid phone number !');
        return false;
    }
    else if(roll_length > 3)
    {
        alert('Roll number must be three(3) digit or less !');
        return false;
    } 
    else if(fname.value.trim() == '')
    {
        alert('First name is required !');
        return false;
    }
    else if(lname.value.trim() == '')
    {
        alert('Last name is required !');
        return false;
    }
    else if(gname.value.trim() == '')
    {
        alert('Guardian name is required !');
        return false;
    }
    else if(nl.value.trim() == '')
    {
        alert('Nationality is required !');
        return false;
    }
    else if(add.value.trim() == '')
    {
        alert('Address is required !');
        return false;
    }
    else
    {
        return true;
    }     

}
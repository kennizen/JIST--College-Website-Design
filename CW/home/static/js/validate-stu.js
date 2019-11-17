function validate(){
    var phone = document.getElementById('phone');

    var phone_value = phone.value;
    var phone_length = phone_value.length;
       

    if(phone_length < 10 || phone_length > 10)
    {
        alert('Invalid phone number !');
        return false;
    }
    else 
    {
        return true;
    }      

}
function validate(){
    var feedback = document.getElementById('feedback');
    
   

    if(feedback.value == '')
    {
        alert('Feedback field cannot be empty!');
        return false;
    }
    else 
    {
        return true;
    }      

}
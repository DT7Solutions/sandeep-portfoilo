
// Contact Form
$(document).ready(function(){
    $('#contact-btn').click(function(){

        let name = $('#name').val();
        let email = $('#email').val();
        let message = $('message').val();
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();


        let data = new FormData
        data.append("name",name),
        data.append("email",email),
        data.append("message",message),
        data.append("csrfmiddlewaretoken",csrfmiddlewaretoken)

        $.ajax({
            type:'POST',
            url:'/',
            processData:false,
            contentType:false,
            cache:false,
            data:data,

            success:function(data,status,xhr){
                $('#contact-submit')[0].reset();
                if(data.success === true){
                    alert('Your Request submited sucessfully!')
                }else{
                    alert(data.error)
                }
            },
            error:function(data){
                alert("form submitted failed")
            }
            
            
            
        })

    })
})



let form_submit = document.getElementById("contact-submit");
form_submit.addEventListener('submit',function(event){
    event.preventDefault();

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    if (name === '' || email === '' || message === ''){
        document.write("All fields Required")
        return;
    }
    this.submit();
})
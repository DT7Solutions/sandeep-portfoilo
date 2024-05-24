
// Contact Form
$(document).ready(function(){
    $('#contact-btn').click(function(){

        let name = $('#name').val();
        let email = $('#email').val();
        let message = $('#message').val();
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();


        let data = new FormData()
        data.append("name",name),
        data.append("email",email),
        data.append("message",message),
        data.append('form_type',"contact")
        
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
                    alert("Please fill the all fields")
                }
            },
            error:function(data){
                alert("form submitted failed")
            } 
            
        })

    })
})



// invite form 

$(document).ready(function(){
    $('#btn-submit').click(function(){
        let name = $('#full_name').val();
        let email = $('#invite_email').val();
        let message = $('#reach-us-message').val();   
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        

        let data = new FormData()
        data.append('name',name),
        data.append('email',email),
        data.append('message',message)
        data.append('form_type',"invite")
        data.append("csrfmiddlewaretoken",csrfmiddlewaretoken)


        $.ajax({
            type: 'POST',
            url: '/',
            data: data,
            contentType: false,
            processData: false,
            success: function(data){
                $('.login-form')[0].reset();
                if(data.success === true){
                    alert('Your Request submited sucessfully!')
                }else{
                    alert("Please fill the all fields")
                }
            },
            error:function(data){
                alert("form submitted failed")
            } 
        });
    })
})
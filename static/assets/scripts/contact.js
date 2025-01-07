
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




// portfolio form
$(document).ready(function(){
    $('#popupsubmit').click(function(){

        let popname = $('#popname').val();
        let popemail = $('#popemail').val();
        let popphone = $('#popphone').val();  
        let popcity = $('#popcity').val();  
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();


        if(popname==""){
            alert("Name field required")
            return;
        }

        if(popemail==""){
            alert("Email field required")
            return;
        }

        if(popphone==""){
            alert("Phone field required")
            return;
        }

        if(popcity==""){
            alert("City field required")
            return;
        }


        let data = new FormData()
        data.append('popname',popname),
        data.append('popemail',popemail),
        data.append('popphone',popphone),
        data.append('popcity',popcity)
        data.append("csrfmiddlewaretoken",csrfmiddlewaretoken)


        $.ajax({
            url: 'submit-form/',
            method: 'POST',
            processData: false,
            contentType: false,
            cache: false,
            mimeType: "multipart/form-data",
            data: data,

            success: function (response) {
                $('#portfolio-form')[0].reset(); // Reset the form on success
                alert('Form submitted successfully');
                window.location.href = 'https://calendly.com/';
            },
            error: function (response) {
                alert('There was an error submitting the form. Please try again.');
                // console.error('Error:', xhr.responseText);
            }
        });
    })
})
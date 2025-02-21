
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


$(document).ready(function () {
    $("#news-letter-submit").click(function () {

       let name        =  $("#fullname").val().trim();;
       let phonenumber =  $("#phone_number").val().trim();
       let email       =  $("#emailid").val().trim();
       let city        = $("#city").val();
       let other       =  $("#other_problem").val();

       if (!name || !phonenumber || !email) {
        alert("Please fill in required the details.");
        return false; // Prevents form submission
    }

        let data = new FormData();
        data.append('full_name', name);
        data.append('phone_number', phonenumber);
        data.append('invite_email', email);
        data.append('city', city);
        data.append('other_problem',other );

        var lookingFor = [];
        $("input[name='looking_for']:checked").each(function () {
            lookingFor.push($(this).val());
        });

        data.append('looking_for[]', lookingFor);

        $.ajax({
            type: "POST",
            url: "/save-newsletter/",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            dataType: "json",
            mimeType: "multipart/form-data",

            success: function (response) {
                if (response.status === "success") {
                    alert(response.message);
                    $(".login-form")[0].reset(); 
                    $("#news-letter-Popup").modal('hide');
                    $("#news-letter-download").modal('show');
                } else {
                    alert("Error: " + response.message);
                }
            },
            error: function () {
                alert("An error occurred. Please try again.");
            }
        });
    });

    // Show "other problem" textarea if "My problem is not listed" is checked
    $("#other_option").change(function () {
        if ($(this).is(":checked")) {
            $("#other_problem_box").show();
        } else {
            $("#other_problem_box").hide();
        }
    });
});



document.getElementById("download-newsletter").addEventListener("click", function() {
    const pdfUrl = "https://magsmen.in/brand_corner_trademarks_and_deceptive_practices/";
    const printWindow = window.open(pdfUrl, "_blank");
    printWindow.onload = function() {
        printWindow.print();
    };
});
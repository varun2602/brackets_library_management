document.addEventListener('DOMContentLoaded', function(){
    // When submit button is pressed 
    document.addEventListener('submit', function(){
        event.preventDefault();

        let formdata = new FormData();
        formdata.append('name', document.querySelector('#name').value)
        formdata.append('username', document.querySelector('#username').value)
        formdata.append('email', document.querySelector('#email').value)
        formdata.append('password', document.querySelector('#password').value)
        formdata.append('cpassword', document.querySelector('#cpassword').value)

        fetch('/register', {
            method:'POST',
            body:formdata
        }).then(response => response.json()).then(data => {
            document.querySelector('#register_response').innerHTML = data.message;
            let form = document.querySelector('form')
            form.reset();
            document.querySelector('#username_available').style.display = 'none'
            document.querySelector('#username_unavailable').style.display = 'none'
            // console.log(data)
        }).catch(error => console.log(error))

        

    })
    // Validating if username is available 
    let user_input_field = document.querySelector('#username')
    
    user_input_field.addEventListener('input', function(){
        let form_data = new FormData();
        form_data.append('username', document.querySelector('#username').value)
        let username_available = document.querySelector('#username_available')
        let username_unavailable = document.querySelector('#username_unavailable')
        fetch('/validate_name',{
            method:'POST',
            body:form_data
        }).then(response => response.json()).then(data => {
            // console.log(`Data` + data)
            if(data.r == 200){
                username_unavailable.style.display  = 'none';
                username_available.style.display = 'block'
                username_available.innerHTML = 'Username available !';
                // console.log(data.r)
                
               
            }
            else if(data.r == 20){
                username_available.style.display = 'none'
                username_unavailable.style.display = 'block'
                username_unavailable.innerHTML = 'Username unavailable'
                // console.log(data.r)
                

            }
        
        }).catch(error => console.log(error))
    })
})
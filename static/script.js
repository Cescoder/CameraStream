const password_entry = document.getElementById('password')
const login_form = document.getElementById('login')

function checkPassword(){
    var password = password_entry.value;
    
    password_entry.value = '';

    const jsonData = JSON.stringify({'password': password});

    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    };

    // Execute the POST request to the FastAPI server
    fetch('http://localhost:5000/login', requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Errore nella richiesta al server');
            }
            return response.json();
        })
        .then(data => {
            message = data.message;
            console.log(message)
            if(message == 'ok'){
                // Get the video feed element from the HTML
                hideLogin()
                const videoFeed = document.getElementById('frame');
            
                // Set the src attribute of the video feed element to the video feed URL
                videoFeed.src = '/video_feed';
        
            }
        })
        .catch(error => {
            console.error('Errore durante la richiesta al server:', error);
        });
}

function hideLogin(){
    login_form.style.display = 'none';
}

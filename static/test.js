document.getElementById('pushButton').addEventListener('click', function () {
    fetch('http://127.0.0.1:8000/test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({message: 'Hello from the frontend!'})
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});

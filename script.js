// When the form is submitted
document.getElementById('questionForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the form from refreshing the page

    // Get the user input
    const userQuestion = document.getElementById('userQuestion').value;

    // Call the FastAPI backend to get the answer
    fetch('http://127.0.0.1:8000/qa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userQuestion })  // Send the question to the backend
    })
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
        // Display the answer returned from the backend
        document.getElementById('answerText').textContent = data.answer;
        document.getElementById('answerSection').style.display = 'block';  // Show the answer section
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('answerText').textContent = "Sorry, I couldn't get an answer.";
        document.getElementById('answerSection').style.display = 'block';  // Show the error message
    });
});

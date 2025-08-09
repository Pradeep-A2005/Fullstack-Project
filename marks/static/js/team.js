function goBack() {
    window.history.back();
}

document.getElementById("markForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    const formElements = event.target.elements;
    let allValid = true;

    for (let i = 0; i < formElements.length; i++) {
        if (formElements[i].type === "number") {
            const value = formElements[i].value;
            if (value < 0 || value > 10) {
                allValid = false;
                alert("Marks must be between 0 and 10.");
                break;
            }
        }
    }

    if (allValid) {
        window.location.href = 'review_mark.html'; 
    }
});

document.getElementById("markForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    fetch("{% url 'save_team_mark' %}", {
        method: "POST",
        headers: {
            "X-CSRFToken": "{{ csrf_token }}",
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            window.location.href = '{% url "review_mark" %}'; 
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred.');
    });
});

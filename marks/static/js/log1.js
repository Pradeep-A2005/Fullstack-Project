document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username === "review@bitsathy.ac.in" && password === "2001") {
        window.location.href = "reviewer_dashboard.html";
    } else {
        alert("Invalid username or password");
    }
});

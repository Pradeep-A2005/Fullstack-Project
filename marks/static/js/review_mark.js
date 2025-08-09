function goBack() {
    window.history.back();
}
document.getElementById("reviewerMarkForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const formElements = event.target.elements;
    let allValid = true;

    for (let i = 0; i < formElements.length; i++) {
        if (formElements[i].type === "number") {
            const value = formElements[i].value;
            if (value === "" || value < 0 || value > 10) {
                allValid = false;
                alert("All marks must be filled and between 0 and 10.");
                break;
            }
        }
    }

    if (allValid) {
        alert("Marks submitted successfully in Database!");
    }
});

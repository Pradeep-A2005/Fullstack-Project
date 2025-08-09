function goBack() {
    window.history.back();
}

document.getElementById('markForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Marks Submitted Successfully in Database');
});

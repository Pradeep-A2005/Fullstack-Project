// Function to filter the student table based on search input
function filterTable() {
    const searchInput = document.getElementById("searchBar").value.toLowerCase();
    const tableRows = document.querySelectorAll("#studentTable tr");

    tableRows.forEach(row => {
        const cells = row.getElementsByTagName("td");
        const ptacId = cells[1]?.textContent || "";
        const name = cells[2]?.textContent || "";

        if (ptacId.toLowerCase().includes(searchInput) || name.toLowerCase().includes(searchInput)) {
            row.style.display = ""; // Show row
        } else {
            row.style.display = "none"; // Hide row
        }
    });
}

// Function to open the PDF modal and show the selected PDF
function viewPDF(pdfUrl) {
    const modal = document.getElementById("myModal");
    const pdfViewer = document.getElementById("pdfViewer");

    // Set the source of the iframe to the PDF URL
    pdfViewer.src = pdfUrl;
    modal.style.display = "block";
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById("myModal");
    modal.style.display = "none";
}

// Close the modal when clicking anywhere outside of it
window.onclick = function(event) {
    const modal = document.getElementById("myModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

// Function to handle select-all checkbox functionality
document.getElementById("selectAll").addEventListener("change", function () {
    const checkboxes = document.querySelectorAll(".select-row");
    const isChecked = this.checked;

    checkboxes.forEach(checkbox => {
        checkbox.checked = isChecked;
    });

    updateSelectedCount();
});

// Function to update the selected count based on checked checkboxes
function updateSelectedCount() {
    const checkboxes = document.querySelectorAll(".select-row:checked");
    document.getElementById("selectedCount").textContent = checkboxes.length;
}

// Event listener to update the selected count when individual checkboxes are checked/unchecked
document.querySelectorAll(".select-row").forEach(checkbox => {
    checkbox.addEventListener("change", updateSelectedCount);
});

// Function to download the selected student PTAC IDs and Names
function downloadSelected() {
    const selectedRows = document.querySelectorAll(".select-row:checked");
    const data = [];

    selectedRows.forEach(row => {
        const ptacId = row.closest("tr").getElementsByTagName("td")[1].textContent;
        const name = row.closest("tr").getElementsByTagName("td")[2].textContent;
        data.push(`${ptacId}, ${name}`);
    });

    const csvContent = "data:text/csv;charset=utf-8," + data.join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "selected_students.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
function downloadSelected() {
    const checkboxes = document.querySelectorAll('.select-row:checked');
    const studentDetails = [];

    checkboxes.forEach((checkbox) => {
        const row = checkbox.closest('tr');
        const ptacId = row.cells[1].innerText; 
        const name = row.cells[2].innerText; 
        const academicYear = row.cells[3].innerText; 
        const semester = row.cells[4].innerText; 
        const projectCategory = row.cells[5].innerText; 
        const projectTitle = row.cells[6].innerText; 

        studentDetails.push([ptacId, name, academicYear, semester, projectCategory, projectTitle]);
    });

    if (studentDetails.length === 0) {
        alert("No students selected for download.");
        return;
    }

    let csvContent = "data:text/csv;charset=utf-8," 
        + "PTAC-ID,Student Name,Academic Year,Semester,Project Category,Project Title\n" 
        + studentDetails.map(e => e.join(",")).join("\n");

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "selected_students.csv");
    document.body.appendChild(link); 

    link.click(); 
    document.body.removeChild(link); 
}        


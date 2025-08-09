// Select all checkboxes
const selectAll = document.getElementById('selectAll');
const checkboxes = document.querySelectorAll('.select-row');
const selectedLabel = document.getElementById('selectedLabel');
const selectedCount = document.getElementById('selectedCount');

// Function to update selected count
function updateSelectedCount() {
    let count = 0;
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) count++;
    });
    selectedCount.textContent = count;
    selectedLabel.style.display = count > 0 ? 'flex' : 'none';
}

// Event listener for 'Select All'
selectAll.addEventListener('change', () => {
    checkboxes.forEach(checkbox => {
        checkbox.checked = selectAll.checked;
    });
    updateSelectedCount();
});

// Event listeners for individual checkboxes
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateSelectedCount);
});

// Pagination variables
let currentPage = 1;
const studentsPerPage = 10;  // You can adjust this value based on your requirement

function updatePagination() {
    const rows = document.querySelectorAll('#studentTable tr');
    const totalStudents = rows.length;
    
    // Calculate the start and end range for the current page
    const start = (currentPage - 1) * studentsPerPage + 1;
    const end = Math.min(currentPage * studentsPerPage, totalStudents);

    // Update total students shown on the page
    document.getElementById('totalStudents').textContent = `Showing ${start} - ${end} `;

    // Show only the rows for the current page
    rows.forEach((row, index) => {
        row.style.display = (index >= start - 1 && index < end) ? '' : 'none';
    });

    // Disable "Previous" button on first page
    document.querySelector('.prev-button').disabled = currentPage === 1;

    // Disable "Next" button on last page
    document.querySelector('.next-button').disabled = end >= totalStudents;
}

// Event listener for 'Next' button
document.querySelector('.next-button').addEventListener('click', () => {
    currentPage++;
    updatePagination();
});

// Event listener for 'Previous' button
document.querySelector('.prev-button').addEventListener('click', () => {
    if (currentPage > 1) currentPage--;
    updatePagination();
});

// Initial Pagination setup
updatePagination();

function filterTable() {
    const input = document.getElementById("searchBar").value.toUpperCase();
    const table = document.getElementById("studentTable");
    const tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {
        const tdPTAC = tr[i].getElementsByTagName("td")[1];
        const tdName = tr[i].getElementsByTagName("td")[2];
        
        if (tdPTAC || tdName) {
            const ptacValue = tdPTAC.textContent || tdPTAC.innerText;
            const nameValue = tdName.textContent || tdName.innerText;
            
            if (ptacValue.toUpperCase().indexOf(input) > -1 || nameValue.toUpperCase().indexOf(input) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }       
    }
}
function downloadSelected() {
    const checkboxes = document.querySelectorAll('.select-row:checked');
    const studentDetails = [];

    checkboxes.forEach((checkbox) => {
        const row = checkbox.closest('tr');
        const ptacId = row.cells[1].innerText; // PTAC-ID
        const name = row.cells[2].innerText; // Student Name
        const academicYear = row.cells[3].innerText; // Academic Year
        const semester = row.cells[4].innerText; // Semester
        const projectCategory = row.cells[5].innerText; // Project Category
        const projectTitle = row.cells[6].innerText; // Project Title

        studentDetails.push([ptacId, name, academicYear, semester, projectCategory, projectTitle]);
    });

    if (studentDetails.length === 0) {
        alert("No students selected for download.");
        return;
    }

    // Convert to CSV format
    let csvContent = "data:text/csv;charset=utf-8," 
        + "PTAC-ID,Student Name,Academic Year,Semester,Project Category,Project Title\n" 
        + studentDetails.map(e => e.join(",")).join("\n");

    // Create a download link
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "selected_students.csv");
    document.body.appendChild(link); // Required for FF

    link.click(); // This will download the data file
    document.body.removeChild(link); // Clean up
}        
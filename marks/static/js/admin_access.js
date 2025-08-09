function updateSelectedCount() {
    const checkboxes = document.querySelectorAll('.ptac-checkbox');
    const selectedCount = document.getElementById('selectedCount');
    const downloadButton = document.getElementById('downloadButton');
    const selectedContainer = document.getElementById('selectedContainer');
    let count = 0;
    
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            count++;
        }
    });
    
    selectedCount.textContent = `Selected PTAC IDs: ${count}`;
    
    // Show or hide the counter and download button based on selected checkboxes
    if (count > 0) {
        selectedContainer.style.display = 'flex';  // Show container if any checkbox is selected
    } else {
        selectedContainer.style.display = 'none';  // Hide container if no checkbox is selected
    }
}

// Function to filter the table based on search input
function filterTable() {
    const input = document.getElementById("searchBar").value.toUpperCase();
    const table = document.getElementById("studentTable");
    const tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {
        const tdPTAC = tr[i].getElementsByTagName("td")[1]; // PTAC ID is now the second column
        const tdName = tr[i].getElementsByTagName("td")[2]; // Student name is the third column
        const tdRName = tr[i].getElementsByTagName("td")[8]; // Reviewer name is the seventh column
        if (tdPTAC || tdName || tdRName) {
            const ptacValue = tdPTAC.textContent || tdPTAC.innerText;
            const nameValue = tdName.textContent || tdName.innerText;
            const rnameValue = tdRName.textContent || tdRName.innerText;

            if (ptacValue.toUpperCase().indexOf(input) > -1 || nameValue.toUpperCase().indexOf(input) > -1 || rnameValue.toUpperCase().indexOf(input) > -1) {
                tr[i].style.display = ""; 
            } else {
                tr[i].style.display = "none"; 
            }
        }       
    }
}

// Function to download all selected student details
function downloadSelected() {
    const checkboxes = document.querySelectorAll('.ptac-checkbox');
    let selectedDetails = [];

    checkboxes.forEach((checkbox, index) => {
        if (checkbox.checked) {
            const row = checkbox.closest('tr');
            const details = Array.from(row.getElementsByTagName('td')).map(td => td.innerText);
            selectedDetails.push(details.join(', '));  // Join all row data as a comma-separated string
        }
    });

    if (selectedDetails.length > 0) {
        const blob = new Blob([selectedDetails.join('\n')], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = 'selected_student_details.txt';
        link.click();
    } else {
        alert('No student details selected for download');
    }
}

// Function to toggle select all checkboxes
function toggleSelectAll() {
    const selectAllCheckbox = document.getElementById('selectAll');
    const checkboxes = document.querySelectorAll('.ptac-checkbox');
    
    checkboxes.forEach(checkbox => {
        checkbox.checked = selectAllCheckbox.checked;
    });

    updateSelectedCount();
}
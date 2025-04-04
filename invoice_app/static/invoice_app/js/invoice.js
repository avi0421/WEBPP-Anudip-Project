document.addEventListener('DOMContentLoaded', function () {
    // Add Django form classes to make it work with Bootstrap
    const formControls = document.querySelectorAll('input, textarea, select');
    formControls.forEach(function (element) {
        if (element.tagName === 'SELECT') {
            element.classList.add('form-select');
        } else if (element.type !== 'checkbox') {
            element.classList.add('form-control');
        }
    });

    // Initialize calculations
    calculateTotals();

    // Add event listeners to quantity and price fields
    attachEventListeners();

    // Setup formset functionality
    setupFormset();
});

function calculateItemTotal(row) {
    const quantity = parseFloat(row.querySelector('[name$="-quantity"]').value) || 0;
    const unitPrice = parseFloat(row.querySelector('[name$="-unit_price"]').value) || 0;
    const total = quantity * unitPrice;

    // Update the item total cell
    const totalCell = row.querySelector('.item-total');
    if (totalCell) {
        totalCell.textContent = '$' + total.toFixed(2);
    }

    return total;
}

function calculateTotals() {
    let subtotal = 0;
    const rows = document.querySelectorAll('.item-row');

    rows.forEach(function (row) {
        // Skip deleted rows
        const deleteCheckbox = row.querySelector('[name$="-DELETE"]');
        if (deleteCheckbox && deleteCheckbox.checked) {
            return;
        }

        subtotal += calculateItemTotal(row);
    });

    // Update subtotal and total display
    const subtotalElement = document.getElementById('subtotal');
    const totalElement = document.getElementById('total');

    if (subtotalElement) {
        subtotalElement.textContent = '$' + subtotal.toFixed(2);
    }

    if (totalElement) {
        totalElement.textContent = '$' + subtotal.toFixed(2);
    }
}

function attachEventListeners() {
    // For existing rows
    const rows = document.querySelectorAll('.item-row');
    rows.forEach(function (row) {
        const quantityInput = row.querySelector('[name$="-quantity"]');
        const priceInput = row.querySelector('[name$="-unit_price"]');
        const deleteCheckbox = row.querySelector('[name$="-DELETE"]');

        if (quantityInput) {
            quantityInput.addEventListener('input', calculateTotals);
        }

        if (priceInput) {
            priceInput.addEventListener('input', calculateTotals);
        }

        if (deleteCheckbox) {
            deleteCheckbox.addEventListener('change', function () {
                if (this.checked) {
                    row.style.opacity = '0.5';
                } else {
                    row.style.opacity = '1';
                }
                calculateTotals();
            });

            // Replace checkbox with a button for better UX
            const deleteButton = document.createElement('button');
            deleteButton.type = 'button';
            deleteButton.className = 'btn btn-sm btn-outline-danger';
            deleteButton.innerHTML = '<i class="bi bi-trash"></i>';
            deleteButton.addEventListener('click', function () {
                deleteCheckbox.checked = true;
                row.style.opacity = '0.5';
                calculateTotals();
            });

            const parentCell = deleteCheckbox.parentElement;
            parentCell.innerHTML = '';
            parentCell.appendChild(deleteCheckbox);
            deleteCheckbox.style.display = 'none';
            parentCell.appendChild(deleteButton);
        }
    });
}

function setupFormset() {
    const addItemButton = document.getElementById('add-item');
    if (!addItemButton) return;

    addItemButton.addEventListener('click', function () {
        const itemsTable = document.getElementById('items-table').getElementsByTagName('tbody')[0];
        const formCount = document.getElementById('id_items-TOTAL_FORMS');
        const newIndex = parseInt(formCount.value);

        // Clone the first row
        const firstRow = itemsTable.querySelector('.item-row');
        const newRow = firstRow.cloneNode(true);

        // Update IDs and names in the new row
        const inputs = newRow.querySelectorAll('input, select, textarea');
        inputs.forEach(function (input) {
            const name = input.getAttribute('name');
            const id = input.getAttribute('id');

            if (name) {
                input.setAttribute('name', name.replace(/\d+/, newIndex));
            }

            if (id) {
                input.setAttribute('id', id.replace(/\d+/, newIndex));
            }

            // Clear values
            if (input.type !== 'checkbox') {
                input.value = '';
            } else {
                input.checked = false;
            }
        });

        // Reset the total
        const totalCell = newRow.querySelector('.item-total');
        if (totalCell) {
            totalCell.textContent = '$0.00';
        }

        // Append the new row and increment the form count
        itemsTable.appendChild(newRow);
        formCount.value = newIndex + 1;

        // Attach event listeners to the new row
        const quantityInput = newRow.querySelector('[name$="-quantity"]');
        const priceInput = newRow.querySelector('[name$="-unit_price"]');
        const deleteCheckbox = newRow.querySelector('[name$="-DELETE"]');

        if (quantityInput) {
            quantityInput.addEventListener('input', calculateTotals);
        }

        if (priceInput) {
            priceInput.addEventListener('input', calculateTotals);
        }

        if (deleteCheckbox) {
            // Replace checkbox with a button
            const deleteButton = document.createElement('button');
            deleteButton.type = 'button';
            deleteButton.className = 'btn btn-sm btn-outline-danger';
            deleteButton.innerHTML = '<i class="bi bi-trash"></i>';
            deleteButton.addEventListener('click', function () {
                deleteCheckbox.checked = true;
                newRow.style.opacity = '0.5';
                calculateTotals();
            });

            const parentCell = deleteCheckbox.parentElement;
            parentCell.innerHTML = '';
            parentCell.appendChild(deleteCheckbox);
            deleteCheckbox.style.display = 'none';
            parentCell.appendChild(deleteButton);
        }
    });
}
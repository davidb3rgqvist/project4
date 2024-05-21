document.addEventListener('DOMContentLoaded', (event) => {
    const createButton = document.querySelector('a[href*="create"] button');

    if (createButton) {
        createButton.addEventListener('click', (event) => {
            const confirmCreate = confirm("Are you sure you want to create a new recipe?");
            if (!confirmCreate) {
                event.preventDefault();
            }
        });
    }
});

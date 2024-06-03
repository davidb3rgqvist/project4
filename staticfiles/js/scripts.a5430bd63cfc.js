// Handling tooglebars in recipes
function toggleSection(sectionId) {
    var content = document.getElementById(sectionId);
    if (content.style.display === "none") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
}

// Handling tooglebars in filters
function toggleFilterSection() {
    var filterContent = document.getElementById("filter-content");
    filterContent.style.display = (filterContent.style.display === "none") ? "block" : "none";
}

// Handling update field for comments
document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll('.edit-comment-btn');
    editButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment-id');
            const commentText = document.querySelector(`#comment-${commentId} .comment-text`);
            const editForm = document.querySelector(`#edit-comment-form-${commentId}`);

            commentText.style.display = 'none';
            editForm.style.display = 'block';
        });
    });
});
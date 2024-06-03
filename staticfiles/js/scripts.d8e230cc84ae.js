function toggleSection(sectionId) {
    var content = document.getElementById(sectionId);
    if (content.style.display === "none") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
}

function toggleFilterSection() {
    var filterContent = document.getElementById("filter-content");
    filterContent.style.display = (filterContent.style.display === "none") ? "block" : "none";
}


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


// footer.js

$(window).scroll(function() {
    var footerHeight = $('#footer').outerHeight();
    var scrollTop = $(window).scrollTop();
    var windowHeight = $(window).height();
    var scrollBottom = scrollTop + windowHeight;

    if ((scrollBottom + footerHeight) >= $(document).height()) {
        $('#footer').removeClass('hidden');
    } else {
        $('#footer').addClass('hidden');
    }
});
function toggleSection(sectionId) {
    var content = document.getElementById(sectionId);
    if (content.style.display === "none") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
}
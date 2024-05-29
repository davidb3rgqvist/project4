$(document).ready(function() {
    // Get the ingredients entered by the user
    var ingredients = $('#id_ingredients').val().split('\n');
    
    // Prepopulate the steps editor with ingredients
    var prepopulatedSteps = '';
    for (var i = 0; i < ingredients.length; i++) {
        prepopulatedSteps += '<p><strong>' + ingredients[i] + '</strong></p>';
    }
    
    $('#id_steps').summernote({
        height: 300,
        minHeight: null,
        maxHeight: null,
        focus: true,
        toolbar: [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['font', ['strikethrough', 'superscript', 'subscript']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']]
        ],
        callbacks: {
            onInit: function() {
                // Highlight prepopulated ingredients
                $('.note-editable p strong').addClass('highlighted');
            }
        },
        // Prepopulate steps with ingredients
        callbacks: {
            onInit: function() {
                var $summernote = $(this);
                $summernote.summernote('pasteHTML', prepopulatedSteps);
            }
        }
    });
});



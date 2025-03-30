$(document).ready(function() {
    $("#id_operation_type").change(function() {
        $.ajax({
            url: "/reference/ajax/load-categories/",
            data: {
                'operation_type': $(this).val()
            },
            success: function(data) {
                $("#id_category").html(data);
                $("#id_subcategory").html('<option value="">---------</option>');
            }
        });
    });

    $("#id_category").change(function() {
        if ($(this).val()) {
            $.ajax({
                url: "/reference/ajax/load-subcategories/",
                data: {
                    'category': $(this).val()
                },
                success: function(data) {
                    $("#id_subcategory").html(data);
                }
            });
        }
    });
});
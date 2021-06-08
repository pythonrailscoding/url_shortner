$(document).on("submit", "#post-form", function(e){
    e.preventDefault();
    document.getElementById("out_url").innerHTML = "Processing and generating your URL";
    $.ajax({
        type: 'POST',
        url: "create/",
        data: {
            link:$('#link').val(),
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function(data){
            $("#out_url").html("");
            $("#out_url").html(data);
        }
    });
});
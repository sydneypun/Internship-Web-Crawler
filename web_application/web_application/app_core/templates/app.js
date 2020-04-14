$(document).ready(function() {
    $("#lesen").click(function() {
        $.ajax({
            url : "myfile.txt",
            dataType: "text",
            success : function (data) {
                $(".text").html(data);
            }
        });
    });
});

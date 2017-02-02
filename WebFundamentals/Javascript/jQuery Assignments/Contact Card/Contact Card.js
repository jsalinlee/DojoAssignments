$("form").submit(function(){
    var firstName = $("#first-name").val();
    var lastName = $("#last-name").val();
    var description = $("#description-input").val();
    $(".card-area").append("<div class='contact-card'><h2>" + firstName + " " + lastName + "</h2><div class='description'>" + description + "</div></div>")
    $(".description").hide();
    return false;
});
$(document).on("click", ".contact-card", function(){
    $(this).children().toggle();
});

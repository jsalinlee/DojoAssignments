var cardCount = 1;
$("form").submit(function(){
    var firstName = $("#first-name").val();
    var lastName = $("#last-name").val();
    var description = $("#description-input").val();
    cardCount++;
    $(".card-area").append("<div class='contact-card'><h2>" + firstName + " " + lastName + "</h2><div id='" + cardCount + "' class='description'>" + description + "</div></div>");
    $("#" + cardCount).hide();
    return false;
});
$(document).on("click", ".contact-card", function(){
    $(this).children().toggle();
});

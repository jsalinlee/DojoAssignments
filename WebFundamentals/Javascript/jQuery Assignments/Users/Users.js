$("form").submit(function(){
    var firstName = $("#first-name").val();
    var lastName = $("#last-name").val();
    var email = $("#email").val();
    var contactNum = $("#contact-num").val();
    $("tbody").append("<tr><td>" + firstName + "</td>" + "<td>" + lastName +
    "</td>" + "<td>" + email + "</td>" + "<td>" + contactNum + "</td></tr>");
    return false;
});

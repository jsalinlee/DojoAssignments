var cat;
var ninja;
$("img").click(function(){
    cat = $(this).attr("src");
    ninja = $(this).attr("ninja-src")
    if ($(this).attr("src") == cat){
        $(this).attr("src", ninja);
        $(this).attr("src", ninja);
        $(this).attr("ninja-src", cat);
    }
});

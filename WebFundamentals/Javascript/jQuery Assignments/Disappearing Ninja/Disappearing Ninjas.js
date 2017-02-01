$("img").click(function(){
    $(this).fadeTo("slow", 0)
});
$("button").click(function(){
    $("img").fadeTo("slow", 1);
})

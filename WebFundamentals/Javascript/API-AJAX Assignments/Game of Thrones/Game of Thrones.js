var url;
$("#description").hide();
$(document).on("click", "img", function(){
    $("#description").show();
    url = "http://www.anapioficeandfire.com/api/houses/" + $(this).attr("index");
    $.get(url, function(res){
        $("#description").html("<h4>Name: </h4><p>" + res.name + "</p><h4>Coat of Arms: </h4><p>" + res.coatOfArms + "</p><h4>Region: </h4><p>" + res.region + "</p><h4>Motto: </h4><p>" + res.words + "</p>");
        console.log(res);
    }, "json");
});

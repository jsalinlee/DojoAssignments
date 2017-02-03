 // your code here (build up your url)

$('form').submit(function() {
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + $("#city-input").val() + "&&appid=8232a82fcac8d98761adb80edb0cdb16";
    $.get(url, function(res) {
        $("body").append("<h1>" + res.name + "</h1>");
        $("body").append("<div>Temperature: " + Math.trunc(res.main.temp * 9/5 - 459.67) + " F</div>");
        console.log(res);
        $("form")[0].reset();
    }, 'json');
    return false;
});

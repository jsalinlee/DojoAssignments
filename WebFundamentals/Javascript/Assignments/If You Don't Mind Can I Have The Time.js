var hour = 10;
var minute = 30;
var period = "PM";
var timeOfDay = "";
var description = "";
var special = "";

if (period === "AM"){
    if (hour === 12){
        special = "midnight";
    }
    else{
        timeOfDay = "in the morning";
    }
}
else if (period === "PM"){
    if (hour === 12){
        special = "noon";
    }
    else if (hour <= 4){
        timeOfDay = "in the afternoon";
    }
    else if (hour >= 7){
        timeOfDay = "at night";
    }
    else {
        timeOfDay = "in the evening";
    }
}
if (minute === 15){
    description = " quarter after";
}
else if (minute === 30){
    description = " half past";
}
else if (minute === 45){
    if (hour === 12){
        hour = 1;
    }
    else{
        hour += 1;
    }
    description = " quarter to";
}
else{
    description = " " + minute + " after";
}
if (special == "midnight" || special == "noon"){
    console.log("It's" + description + " "+ special, timeOfDay);
}
else
    console.log("It's" + description + " " + hour, timeOfDay);

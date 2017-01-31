function knownRange(days){
    var reward = 0.01;
    var increase = 0.01;
    for (var i = 1; i < days; i++){
        console.log(reward);
        increase *= 2;
        reward += increase;
    }
console.log("The reward after 30 days is " + reward);
}

function unknownRange(desiredReward){
    var reward = 0.01;
    var increase = 0.01;
    var dayCount = 1;
    while (reward < desiredReward){
        increase *= 2;
        reward += increase;
        dayCount++;
    }
    console.log("The servant would make " + desiredReward + " after " + dayCount + " day(s)");
}
knownRange(30);
unknownRange(10000);
unknownRange(1000000000);
unknownRange(Infinity);

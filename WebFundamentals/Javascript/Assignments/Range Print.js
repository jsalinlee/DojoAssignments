function rangePrint(startPoint, endPoint, skipAmount){
    var printValue = startPoint;
    if (skipAmount == undefined){
        skipAmount = 1;
    }
    if (endPoint == undefined){
        endPoint = printValue;
        printValue = 0;
    }
    while (printValue < endPoint){
        console.log(printValue);
        printValue += skipAmount;
    }
}
rangePrint(-7);

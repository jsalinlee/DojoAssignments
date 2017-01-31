function fancyArray(arr, symbol, reversed){
    var temp = 0;
    if (reversed === true){
        for (var i = 0; i < (arr.length - 1) / 2; i++){
            temp = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }
    }
    for (var i = 0; i < arr.length; i++){
        console.log(i + symbol + arr[i]);
    }
}
fancyArray(["James", "Jill", "Jane", "Jack"], "-->", true);

function lottery(numQuarters){
    var coinAmount = 0;
    var playNumber = 0;
    var winningNumber = 0;
    var maxWinnings = 200;

    while (numQuarters >= 0){
        playNumber = Math.floor(Math.random() * 100) + 1;
        winningNumber = Math.floor(Math.random() * 100) + 1;
        console.log("Your Number: " + playNumber);
        console.log("Winning Number: " + winningNumber);

        numQuarters--;
        if (playNumber === winningNumber){
            console.log("You win!");
            coinAmount = Math.floor(Math.random() * 50) + 51;
            numQuarters += coinAmount;
            if (numQuarters < maxWinnings) {
                continue;
            }
            else{
                return numQuarters;
            }
        }
        else{
            console.log("You lose :(");
        }
        if (numQuarters === 0){
            return 0;
        }
    }
}
lottery(10);

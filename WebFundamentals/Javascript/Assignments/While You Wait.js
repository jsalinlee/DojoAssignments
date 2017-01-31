function whileYouWait(){
  var daysUntilMyBirthday = 60;

  for(var i = daysUntilMyBirthday; i >= 0 ; i--){
    if(i >= 30){
      console.log(i+" days until my birthday. So so long");
    }
    else if(i < 30 && i > 5){
      console.log(i+" days until my birthday. Whoohoo!");
    }
    else if (i <= 5 && i > 0) {
      console.log(i+" DAYS UNTIL MY BIRTHDAY! PRESENTS!");
      }
    else{
      console.log("IT'S MY BIRTHDAY!");
    }
  }
}

whileYouWait();

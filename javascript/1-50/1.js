function sumMultiplesOfThreeAndFive(ceiling) {
  var result = 0;

  for (var i = 0; i < ceiling; i++){
    if (i % 3 == 0 || i % 5 == 0 ){
      result += i;
    }}
    console.log(result)
  }


sumMultiplesOfThreeAndFive(1000);

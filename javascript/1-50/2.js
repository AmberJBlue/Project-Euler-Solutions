
function evenFib(ceiling){
  let curr = 0,
    next = 1,
    sum = 0,
    result = 0;

  while (curr + next < 4000000) {
    sum = curr + next;
    curr = next;
    next = sum;

    if (sum % 2 === 0) {
      result += sum;
    }
  }
  console.log(result);
}

evenFib(4000000);

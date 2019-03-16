
function solution(number) {
  let prime = 2;

  while(number > prime){
    if(number % prime === 0){
      number /= prime
    }
    prime++;
  }
  console.log(prime)
}

solution(600851475143);

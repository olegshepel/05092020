
function reverseBinary(number) {
  let bn = number.toString(2);
  let rbn = bn.split('').reverse().join('');
  return parseInt(rbn, 2);
}

console.log(reverseBinary(13));

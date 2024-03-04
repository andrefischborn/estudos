function loveCalculator(name1, name2) {
  var loveScore = Math.random();
  loveScore *= 100;
  loveScore = Math.floor(loveScore) + 1;
  console.log(name1 + ", suas chances com " + name2 + " são de: " + loveScore + "%");

  if (loveScore >= 70) {
    console.log("Nasceram para casar!");
  } else {
    console.log("Vaza que vai dar merda!")
  }

}



loveCalculator(prompt("Digite o primeiro nome: "), prompt("Digite o segundo nome: "));
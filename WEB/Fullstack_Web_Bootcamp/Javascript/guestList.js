var guestList = ["André", "Aline", "Ana", "Manu", "Lidia", "Joel"];
console.log(guestList);

var confirmPrompt = prompt("Digite o nome do convidado: ");
if (guestList.includes(confirmPrompt)) {
  console.log("Convidado");
} else {
  console.log("Não está na lista");
}

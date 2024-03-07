var guestList = ["André", "Aline", "Ana", "Manu", "Lidia", "Joel"];
var confirmPrompt = prompt("Digite o nome do convidado: ");
if (guestList.includes(confirmPrompt)) {
  console.log("Convidado");
} else {
  console.log("Não está na lista");
}


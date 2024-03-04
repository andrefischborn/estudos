var text = prompt("Digite sua mensagem aqui: ");
var maxCharacters = 280;
var usado = text.length;
var remaining = maxCharacters - usado;

alert("Você usou " + usado + " caracteres de " + maxCharacters + ". Ainda tem " + remaining + " disponíveis.");
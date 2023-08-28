function toggleMode() {
  const html = document.documentElement
  html.classList.toggle("light") // Jeito curto e rápido

  // Jeito longo de fazer:
  //  if (html.classList.contains("light")) {
  //   html.classList.remove("light")
  //  } else {
  //    html.classList.add("light")
  //  }

  // pegar a tag img
  const img = document.querySelector("#profile img")

  // substituir a imagem
  if (html.classList.contains("light")) {
    img.setAttribute("src", "./assets/avatar-light.png") // se tiver light mode, adicionar a imagem light
    img.setAttribute("alt", "foto de maykbrito sorrindo, usando óculos de sol preto, jaqueta cinza, sem barba e com fundo azul degrade com rosa,")
  } else {
    img.setAttribute("src", "./assets/avatar.png") // se tiver sem lightmode, manter a imagem normal
  }
}

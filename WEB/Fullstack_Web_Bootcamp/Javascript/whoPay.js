let names = ["Angela", "Ben", "Jenny", "Michael", "Chloe", "Jack", "Gabriel", "Maria"];

function whosPaying(names) {
  /******Don't change the code above*******/

  var numOfPeople = names.length;
  var randomPersonPosition = Math.floor(Math.random() * numOfPeople);
  var randomPerson = names[randomPersonPosition];

  return randomPerson + " Is going to pay the lunch today!";

  /******Don't change the code below*******/
}

whosPaying(names);

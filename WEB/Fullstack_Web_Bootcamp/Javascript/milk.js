function getMilk(money, costPerBottle) {   
    console.log("leaveHouse");
    console.log("moveRight");
    console.log("moveRight");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveRight");
    console.log("moveRight");


    console.log("You bought " + calcBootles(money, costPerBottle) + " bootles of milk.")

    console.log("moveLeft");
    console.log("moveLeft");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveLeft");
    console.log("moveLeft");
    console.log("enterHouse");

    return calcChange(money, costPerBottle);
  }


function calcBootles(startingMoney, costPerBottle){
    var numberOfBootles = Math.floor(startingMoney / costPerBottle);
    return numberOfBootles;
}
function calcChange(startingMoney, costPerBottle){
    var change = startingMoney % costPerBottle;
    return change;
}

console.log("Hello, Master. Here is your " + getMilk(8, 1.2) + " change.");
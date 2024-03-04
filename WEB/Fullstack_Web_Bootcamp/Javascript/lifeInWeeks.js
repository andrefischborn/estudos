function lifeInWeeks(age) {
    var yearRemaining = 90 - age;
    var monthsRemaining = age * 12;
    var weeksRemaining = age * 52;
    var daysRemaining = age * 365;

    console.log("You have " + yearRemaining + " years, or " + monthsRemaining + " months, or " + daysRemaining + " days remaining.")
}

lifeInWeeks(38);
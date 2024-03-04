function bmiCalculator(weight, height) {
    let interpretation; // Declarando a variável interpretation
    let calc = weight / Math.pow(height, 2);
  
    if (calc < 18.5) {
      interpretation = "Your BMI is " + calc + ", so you are underweight.";
    } else if (calc >= 18.5 && calc <= 24.9) {
      interpretation = "Your BMI is " + calc + ", so you have a normal weight.";
    } else {
      interpretation = "Your BMI is " + calc + ", so you are overweight.";
    }
    return interpretation;
  }
  
  var bmi = Math.round(bmiCalculator(65, 1.8));
  console.log(bmi);
  
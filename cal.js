function calculate() {

    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let operator = document.getElementById("operator").value;

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById("result").innerHTML = "Answer: Enter both numbers";
        return;
    }

    let answer;

    if (operator == "+") {
        answer = num1 + num2;
    }
    else if (operator == "-") {
        answer = num1 - num2;
    }
    else if (operator == "*") {
        answer = num1 * num2;
    }
    else if (operator == "/") {

        if (num2 == 0) {
            answer = "Cannot divide by zero";
        } else {
            answer = num1 / num2;
        }
    }

    document.getElementById("result").innerHTML = "Answer: " + answer;
}

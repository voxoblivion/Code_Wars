// https://www.codewars.com/kata/binary-addition/train/javascript
function addBinary(a,b) {
    let total = a + b;
    let binary_string = "";
    let c = 1;
    let binary_numbers = [];
    for (let counter = 0; counter < 10; counter++){
        binary_numbers.push(c);
        c = c * 2;
    }
    binary_numbers.reverse();
    let number_found = false;
    for (let i = 0; i < binary_numbers.length; i++){
        let d = binary_numbers[i];
        if (total / d >= 1 && total != 0){
            total = total - d;
            binary_string += "1";
            number_found = true;
        }
        else if (number_found == true){
            binary_string += "0";
        }
    }
    return binary_string;
}

function addBinary2 (a,b){
    return (a+b).toString(2)
}


console.log(addBinary(1,2))
console.log(addBinary2(1,2))

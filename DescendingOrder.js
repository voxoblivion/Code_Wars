// https://www.codewars.com/kata/descending-order/train/javascript

function descendingOrder(num){
    let a = []
    num = num.toString()
    for (let i = 0; i < num.length; i++){
        a.push(num[i])
    }
    a = ((a.sort()).reverse()).join("")
    return parseInt(a)

}

function descendingOrderV2(n){
    return parseInt(String(n).split('').sort().reverse().join(''))
}

console.log(descendingOrder(21445))

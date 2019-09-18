// https://www.codewars.com/kata/52761ee4cffbc69732000738/train/javascript

function  goodVsEvil(good, evil) {
    good = good.split(' ');
    evil = evil.split(' ');
    let good_values = [1, 2, 3, 3, 4, 10];
    let evil_values = [1, 2, 2, 2, 3, 5, 10];
    function total_calc(value, value_map){
        let total_value = 0;
        for (let i = 0; i < value.length; i++ ){
            total_value += value[i] * value_map[i];
        }
        return total_value;
    }
    let total_good = total_calc(good, good_values);
    let total_evil = total_calc(evil, evil_values);
    if (total_good == total_evil){return 'Battle Result: No victor on this battle field'}
    else if(total_good > total_evil){return "Battle Result: Good triumphs over Evil"}
    else{return "Battle Result: Evil eradicates all trace of Good"}

}

function goodVsEvilV2(good, evil){
    let values = [[1, 2, 3, 3, 4, 10], [1, 2, 2, 2, 3, 5, 10]]
    good = good.split(' ').reduce((s,v,i) => s + values[0][i] * v, 0);
    evil = evil.split(' ').reduce((s,v,i) => s + values[1][i] * v, 0);
    if (good == evil) return 'Battle Result: No victor on this battle field'
    else if(good > evil) return "Battle Result: Good triumphs over Evil"
    else return "Battle Result: Evil eradicates all trace of Good"
// The reduce() method executes the callback once for each assigned value present in the array.
}



let array = [1, 2, 1, 1];
let total = array.reduce((a,b,c) => a + b * c, 4); //Uses a as accumulator, b as current value, c as index and 4 has the initial value

console.log(goodVsEvil('1 2 3 4 5 6','1 2 3 4 5 6 7'))

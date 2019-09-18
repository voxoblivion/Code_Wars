// https://www.codewars.com/kata/list-filtering/train/javascript



function filter_list(list){
    return list.filter(word => typeof word != "string")
}
console.log(filter_list([1,'a','b',0,15]));


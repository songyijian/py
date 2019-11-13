
// while在...期间 | loop环


let dicts = {
  'name':'ooo',
  'ags':10,
  'obj':2222
}

// let items = arr.entries(dicts)
// console.log(items);

// var i = 0
// while (i < items.length){
//   console.log(JSON.stringify(items[i]) +" | "+ items[i][0] + ":" + JSON.stringify(items[i][1]))
//   i++
// }
// console.log('>while 对字典完成了一次遍历')


// var i = 0;
// for(i; i<20; i++){
//   console.log(i);
//   if(i>15) break;
// }
// console.log('>for 完成了一次遍历');

// for (const key in dicts) {
//   if (dicts.hasOwnProperty(key)) {
//     const element = dicts[key];
//     console.log(element);
//   }
// }

var arr = ['a', 'b', 'c', 'd', 'e']

for (const key in arr) {
  if (arr.hasOwnProperty(key)) {
    const element = arr[key];
    console.log(element);
  }
}
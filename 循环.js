
// while在...期间 | loop环


let dicts = {
  'name':'ooo',
  'ags':10,
  'obj':2222
}

let items = Object.entries(dicts)
console.log(items);


var i = 0
while (i < items.length){
  console.log(JSON.stringify(items[i]) +" | "+ items[i][0] + ":" + JSON.stringify(items[i][1]))
  i++
}

console.log('>对字典完成了一次遍历')

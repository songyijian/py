// Objcet

var dict = {
  "name": 1,
  "f": true,
  "obj": {
    "c": 'xxxxxxx',
    "f": 3
  }
}

// 删除指定键 delete
// delete dict['name']
// console.log(dict);


// 清空 
// dict = {}
// console.log(dict);


// 判断类型 typeof 
// console.log(typeof dict)  //object

//  转字符串 str
// console.log(typeof JSON.stringify(dict))  //string


// 浅拷贝 Object.assign({}, source); 合并可枚举元素
// let dic2 = Object.assign({}, dict)

// console.log(dict)
// dict.f = false
// console.log(dict)
// console.log(dic2)


// in
// console.log( "name" in dict );



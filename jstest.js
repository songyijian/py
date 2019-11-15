
// 结构赋值


// var [a, b, c] = [1, 2, { 'a': 10, 'b': 20 }]
// console.log(a,b,c);


// var [a, ...b] = [1, 2, { 'a': 10, 'b': 20 }]
// console.log(a,b);


// var { a, b } = { 'a': 10, 'b': 20 }
// console.log(a,b);




// 函数验证

// function tfn(a,...b){
//   console.log(a,b);
// }
// tfn(1,2,3,4)


// # 简单类型不会被改变
// function tfn(a){
//   a = 100
//   console.log(a);
// }

// var a = 1
// tfn(a)
// console.log(a);




// 引用类型会修改外部对象
function tfn(a){
  a['x'] = 100 
  console.log(a);
}

var a = {'x':1}
tfn(a)
console.log(a);




// 异常捕获
// try {
  
// } catch (error) {
  // err 是一个error对象
  
// }
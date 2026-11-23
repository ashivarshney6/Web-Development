// alert("hii everyone")
// let b="ashi varshney"
// console.log(b);
// let username=null
// console.log(username);
// console.log(typeof b);
// bigInt
// const student=[
//     {
//         name:"ashi",
//         age:2,
//         place:"jaipur"
//     },
//     {
//         name:"aniket",
//         age:1,
//         place:"mathura"

//     }
// ]
// console.log(...student);
// console.log(10+20+("5"-"5"))
// console.log(10+20+"5"-"5")
// // console.log(typeof ("5"-"5"))
// console.log("i am learning javascript.")
// alert("welcome to the webpage💓💓💓")
// alert("aap bhut cute ho 😥")


// let a=7
// if(a>8){
//     console.log("hello world")
// }
// else{
//     console.log("bye bye🙋‍♂️")
// }
// ternary operator
// let b=a>10 ? "hello":"bye"
// console.log(b)
// let num=57
// if(num%5==0){
//     console.log("number is divisible by 5")
// }
// else{
//     console.log("number is not divided by 5")
// }let num=prompt("enter your marks")

// if(num>=91&&num<=100){
//     console.log("grade is A")
// }
// else if(num>=81&&num<=90){
//     console.log("grade is B")
// }
// else if(num>=71&&num<=80){
//     console.log("grade is C")
// }
// else{
//     console.log("grade is D")
// }
// let number=prompt("enter the day")
// switch(number){
//     case "sunday":
//         console.log("one")
//         //break
//     case "monday":
//         console.log("two")
//         //break   
//     case "tuesday":
//         console.log("three")
//        // break   
//     case "wednesday":
//         console.log("four")
//         //break  
//     case "thursday":
//         console.log("five") 
//        // break
//     case "friday":
//         console.log("six") 
//         //break
//     case "saturday":
//         console.log("seven") 
//         //break
//     default:
//         console.log("invalid day")


//}
// function calculator(){
// let operator = prompt("enter the opertor")
// let num1 = Number(prompt("enter first number"))
// let num2 = Number(prompt("enter second number"))
// switch(operator){
//     case "+":
//         console.log(num1+num2);
//         break
//     case "-":
//         console.log(num1-num2);
//         break   
// }
// }
// calculator()


// for (let i=1; i<=3; i++){
//     console.log(i);
// }
// let i=1;
// while(i<=5){
//     console.log(i);
//     i=i+3;
// }
// let i=1;
// let sume=0;
// let sumo=0;
// while(i<=50){
//     if(i%2==0){
//         sume=sume+i
//         console.log("even:",i)
//         i=i+1
//     }
//     else{
//         sumo=sumo+i
//         console.log("odd:",i)
//         i=i+1
//     }
// }
// console.log("even sum:",sume)
// console.log("odd sum:",sumo)


// let i=10;
// do{
//     console.log(i);
// }while(i<=5);

// let first="hello"
// let second="student"
// let message=`${first} ${second}!`
// console.log(message)        
// const firstname='ashi'
// const lastname='varshney'
// const fullname=firstname+" "+lastname
// console.log(fullname.length);
// console.log(fullname[0]);
// console.log(`${firstname} is learning python`)
// const raw = '   javascript course    '
// function greet(a,b){
//     console.log(a+b);
// }

// greet(3,4)
// function calculator(a,op,b){
//     if(op==='add'){
//         console.log("add=",a+b)
//     }
//     else if(op==='subtraction'){
//         console.log("subtraction=",a-b)
//     }
//     else if(op==='multiplication'){
//         console.log("multiplication=",a*b)
//     }
//     else if(op==='division'){
//         console.log("division=",a/b)
//     }
// }
// console.log(calculator(20,'add',10))
//() => {} arrow function
// const numbers=[1,2,3,4,5,6];
// const doubled=numbers.map((num) =>{
//     return num*2;
// });
// console.log(doubled);
// console.log(numbers);
// const evens=numbers.filter((num)=>{
//     return num%2===0;
// })
// console.log(evens);
// const evens=numbers.find((num => {
//     return num%2===0;
// }))
// console.log(evens);
// const sum=numbers.reduce((acc,current)=>{
//     return acc+current;
// }, 0);
// console.log(sum);

//object is like dictionary
// const student={
//     name:"aman",
//     "age":21,
//     course:"javascript"
// };
// console.log(student)
// console.log(student.name);
// console.log(student["age"])
// const key="age"
// console.log(student[key]);



// student.city="banaras" //add
// student.age=22; //update
// delete student.city; //delete

// console.log(student)




//four types of creating object
//1. object literal
// const user={name:"aman",age:25}

//2.  new object()
// const user=new Object();
// user.name="aman";
// user.age=20;
// console.log(user)

//3. constructor function - 
// function User(name , age){
//     this.name=name;
//     this.age=age;
// }
// const u1 = new User("aman",21);
// console.log(u1)

//4. class 
// class user {
//     constructor(name) {
//     this.name=name;
//     }
// }
// const user1 = new user("vanshika mam");
// console.log(user1);


//class
// class student {
//     constructor(name,age){
//         this.name=name;
//         this.age=age
//     }
//     display() {
//         console.log(
//             this.name + "learns" + this.age
//         );
//     }
// }
// const s1=new student("aman",21);
// s1.display();


//...spread (to spend the array)
// const first=[10,20];
// const second=[30,40];
// const combined=[...first,...second];
// console.log(combined);
// console.log(...combined);

//rest operator (to collect)

const title=document.getElementById("hello");
console.log(title.textContent);
console.log(title);





 
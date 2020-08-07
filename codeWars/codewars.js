var member = [[50, 10], [40, 20], [10, 1]];
var list = [];

for (age, handicap) in member{
  if(age >= 50 && handicap > 7 ) {
    list.push("Senior");
  } else {
     list.push("Open");
   }
}

console.log(list);

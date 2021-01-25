let age = [10, 20, 30, 40, 45, 50, 60];
age = age.sort((a, b) => a - b);
let c_Group = 10,cnt=0,pntr = 0;
let groups = [];

while (c_Group <= 100) {
  if (age[pntr] <= c_Group) {
    cnt++;
    pntr++;
  } else {
    groups.push(cnt);
    cnt=0;
    c_Group += 10;
  }
}

console.log("Age Total Number of People");
groups.map((group, i) => console.log(`${i * 10 - 9 + 10}-${i * 10 + 10}: ${group}`));

export const digitalRoot = (n:number):number => {
  while (n>9) {
    n = n.toString().split("").map(Number).reduce((a,b)=>a+b,0)
  }
  return n
};

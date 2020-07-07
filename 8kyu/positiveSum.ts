export function positiveSum(arr:number[]):number {
  return arr.reduce((acc,cur)=>cur>0?acc+cur:acc,0)  
}
//https://www.codewars.com/kata/5715eaedb436cf5606000381/

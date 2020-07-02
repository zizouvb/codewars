export function countBits(n: number) {
  return n.toString(2).split("").filter(x=>x==="1").length
}

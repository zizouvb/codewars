export function descendingOrder(n: number) {
  return Number(n.toString().split("").sort().reverse().join(""))
}

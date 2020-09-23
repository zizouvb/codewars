export function findNb(m: number): number {
  let sum = 0
  for (let i=1;sum<=m; i++) {
    sum += i**3
    if (sum===m) return i
  }
  return -1
}

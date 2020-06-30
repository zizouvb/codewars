export function findShort(s: string): number {
  return s.split(" ").reduce((acc, cur) => acc>cur.length?cur.length:acc,Infinity)
}

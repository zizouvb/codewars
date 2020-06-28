export function findOutlier(integers: number[]): number {
  const even = integers.filter(num=>num%2===0)
  const odd = integers.filter(num=>Math.abs(num)%2===1)
  return even.length===1 ? even[0] : odd[0]
}

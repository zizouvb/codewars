export function tribonacci([a, b, c]: [number, number, number], n: number): number[] {
  const ans = [a,b,c]
  if (n<=3) return ans.slice(0,n)
  for (let i=3;i<n;i++){
    ans.push(ans[i-3]+ans[i-2] + ans[i-1])
  }
  return ans
}

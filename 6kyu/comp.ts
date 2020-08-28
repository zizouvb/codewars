export function comp(a1: number[] | null, a2: number[] | null): boolean {
  if (a1===null || a2===null) return false
  if (a1.length!==a2.length) return false
  const sortedA2 = a2.sort((a,b)=>a-b)
  return a1.sort((a,b)=>a-b).every((a,i)=>sortedA2[i]===a*a)
}//https://www.codewars.com/kata/550498447451fbbd7600041c/typescript

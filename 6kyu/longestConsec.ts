export function longestConsec(strarr: string[], k: number): string {
  if (k<=0) return ""
  let ans=""
  for (let i=0;i<=strarr.length-k;i++) {
    let candidate = strarr.slice(i,i+k).join("")
    if (candidate.length>ans.length){
      ans=candidate
    }
  }
  return ans
}

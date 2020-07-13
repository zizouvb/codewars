function persistence(num) {
   let ans=0
   while (num.toString().length>1) {
      ans+=1
      num=num.toString().split("").reduce((a,c)=>a*c,1)
   }
  return ans
}

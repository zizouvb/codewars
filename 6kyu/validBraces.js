function validBraces(braces){
  const corr = {"(":")","[":"]","{":"}"}
  const stack = []
  for (let b of braces) {
    if (["(","[", "{"].indexOf(b)>-1){
      stack.push(b)
    } else {
      const p = stack.pop()
      if (corr[p]!==b)
        return false
    }
  }
  return stack.length===0
}

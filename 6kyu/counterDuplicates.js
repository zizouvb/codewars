function duplicateCount(text){
  const count = {}  
  text.toLowerCase().split("").forEach(l=>{count[l] = (count[l]||0)+1})
  return Object.values(count).filter(c=>c>1).length
}

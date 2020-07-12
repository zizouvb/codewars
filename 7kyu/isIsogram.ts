export function isIsogram(str: string){
  const seen:string[] = [] 
  for (let s of str.toLowerCase().split("")){
    if (seen.indexOf(s)>-1) return false
    seen.push(s)
  }
  return true
}
//https://www.codewars.com/kata/54ba84be607a92aa900000f1

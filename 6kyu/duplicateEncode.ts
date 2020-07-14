export function duplicateEncode(word: string){
    const count: {[letter: string]: number} = {}
    word.toLowerCase().split("").forEach(l=>{
      if (l in count) {
        count[l]+=1
      } else {
        count[l]=1
      }
    })
    return word.toLowerCase().split("").map((l:string)=>count[l]>1?")":"(").join("")
}
//https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/

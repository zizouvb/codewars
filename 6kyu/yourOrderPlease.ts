export function order(words:string):string{
  return words.split(" ").sort((w1, w2)=>
    Number(w1.match(/\d/))-Number(w2.match(/\d/))
  ).join(" ")
}

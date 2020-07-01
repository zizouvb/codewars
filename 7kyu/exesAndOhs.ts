export function xo(str: string) {
  let nbO=0
  let nbX=0
  for (let i=0;i<str.length;i++) {
  if (str[i].toLowerCase()==="x") nbX+=1 
  if (str[i].toLowerCase()==="o") nbO+=1
  }
  return nbO===nbX
}

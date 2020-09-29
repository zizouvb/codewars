export function countSmileys(arr: string[]) {
  const regEx = new RegExp (/[:;][-~]?[)D]/)
  return  arr.filter((s:string) => regEx.test(s)).length
}

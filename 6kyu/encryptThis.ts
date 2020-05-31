export const encryptThis = (str: string): string => {
  // Your code goes here
  if (str.length===0) return ""
  return str.split(" ").map(str => 
            {
              const arrayStr:(string|number)[] = str.split("")
              arrayStr[0] = str.charCodeAt(0)
              const temp = arrayStr[1]
              arrayStr[1] = arrayStr[arrayStr.length-1]
              arrayStr[arrayStr.length-1]=temp
              return arrayStr.join("")
            }).join(" ")
}

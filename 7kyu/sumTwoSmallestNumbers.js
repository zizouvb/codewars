function sumTwoSmallestNumbers(numbers) {  
  return numbers.reduce((acc, cur)=>
                 { if (cur<=acc[1]) {
                     if (cur<acc[0]) {
                       acc[1] = acc[0]
                       acc[0] = cur
                     } else {
                       acc[1] = cur
                     } 
                    }
                    return acc
                 },[Infinity,Infinity])
          .reduce((acc,cur)=>acc+cur)
}//https://www.codewars.com/kata/558fc85d8fd1938afb000014/

export function isValidWalk(walk: string[]) {
  const path=walk.reduce((acc,cur)=>{
     acc.dist+=1
    switch(cur) { 
     case "n": { 
       acc.vertical+=1
       break
     } 
     case "s": { 
        acc.vertical-=1
        break; 
     } 
        case "e": { 
        acc.horizontal+=1
        break; 
     } 
        case "w": { 
        acc.horizontal-=1
        break; 
     } 
     default: { 
        break; 
     }
   } 
   return acc              
  },{dist:0, vertical:0, horizontal:0})
  console.log(path)
  return path.dist===10 && path.vertical===0 && path.horizontal===0
}
//https://www.codewars.com/kata/54da539698b8a2ad76000228/

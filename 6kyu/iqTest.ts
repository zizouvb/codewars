export function iqTest(strings: string): number {
    let nbOdd = 0
    let nbEven = 0
    let lastOdd = 0
    let lastEven = 0
    let numbers = strings.split(" ").map(Number)
    for (let i = 0; i < numbers.length; i++) {
        let num = numbers[i]
        if (num % 2 === 0) {
            nbEven += 1
            lastEven = i + 1
        } else { nbOdd += 1; lastOdd = i + 1 }
        if (nbEven > 1 && nbOdd>0) {
            return lastOdd
        } else if (nbOdd > 1 && nbEven>0) {
            return lastEven
        }
    }
    return 1
} 

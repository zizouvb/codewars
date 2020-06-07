function sumStrings(a,b) { 
    let a_array = a.split("").map(Number)
    let b_array = b.split("").map(Number)
    while (a_array[0]===0) {a_array.shift()}
    while (b_array[0]===0) {b_array.shift()}
    let i = Math.max(a_array.length, b_array.length)
    let ans = []
    let carry = 0
    while (i>0) {
        let a_temp = (a_array.pop() || 0)
        let b_temp = (b_array.pop() || 0)
        ans.unshift(( a_temp + b_temp +carry) % 10);
        carry = Math.floor((a_temp + b_temp + carry) / 10);
        i-=1
    }
    if (carry>0) ans.unshift(carry % 10);
    return ans.join('');
}

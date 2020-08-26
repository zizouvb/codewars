export class G964 {
    public static digPow = (n: number, p: number) => {
        const total = [...n.toString()].reduce((acc,cur,index)=>acc+Number(cur)**(p+index),0)
        return total%n===0?total/n:-1
    }
}

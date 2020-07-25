package kata

func MaximumSubarraySum(numbers []int) int {
    var max,curr int = 0,0
    for i := 0; i < len(numbers); i++ {
      curr += numbers[i]
      if (curr<0) {curr=0}
      if (curr>max) {max=curr}
    }
    return max
}

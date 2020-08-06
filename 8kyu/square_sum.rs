fn square_sum(vec: Vec<i32>) -> i32 {
    return vec.iter().map(|x| x.pow(2)).sum();
}

fn find_smallest_int(arr: &[i32]) -> i32 { 
    arr.iter().cloned().fold(i32::MAX, i32::min)
}

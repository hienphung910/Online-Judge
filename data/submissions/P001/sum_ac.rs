// Bai nop dung cho P001 bang Rust -> ky vong AC.
use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    println!("{}", nums[0] + nums[1]);
}

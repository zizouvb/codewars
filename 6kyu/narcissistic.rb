def narcissistic?(value)
  value == value.to_s.chars.map { |x| x.to_i**value.to_s.size }.sum
end

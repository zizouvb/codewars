function likes(names) {
  if (names.length===0) return "no one likes this"
  if (names.length===1) return names[0] + " likes this"
  if (names.length===2) return names.join(" and ") + " like this"
  if (names.length===3) return names.join(', ').replace(/, ([^,]*)$/, ' and $1') + " like this"
  return names[0] + ", " + names[1] + " and " + (names.length-2) + " others like this"
}

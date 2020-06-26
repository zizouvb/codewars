export function twoOldestAges(ages: number[]): number[] {
  return ages.sort((n1,n2) => n1 - n2).slice(ages.length-2);
}

export function findUniq(arr: number[]): number {
  const ans =  arr.find(n => arr.indexOf(n) === arr.lastIndexOf(n)) || arr[0];
  return ans;
}

public class Kata{
  public static double find_average(int[] array){
    double sum = 0;
    for (int i : array) sum += i;
    return sum/array.length;
  }
}

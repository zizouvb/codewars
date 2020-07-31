import java.lang.Math;
public class NumberFun {
  static boolean isPerfectSquare(long n) 
    { 
        for (int i = 1; i * i <= n; i++) { 
            if ((n % i == 0) && (n / i == i)) { 
                return true; 
            } 
        } 
        return false; 
    } 
  public static long findNextSquare(long sq) {
      if (isPerfectSquare(sq)==false) return -1;
      else {
        return (long) Math.pow((Math.sqrt(sq)+1),2);
      }
  }
}

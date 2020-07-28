public class Triangle
{
    public static bool IsTriangle(int a, int b, int c)
    {
        return a+b>c && b+c>a && a+c>b;      
    }
}

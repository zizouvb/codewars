public static class Kata
{
  public static string Maskify(string cc)
  {
    char[] ch = cc.ToCharArray();
    for (int i = 0;i<cc.Length-4;i++) {
      ch[i]='#';
    }
    return new string(ch);
  }
}

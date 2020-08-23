using System;
using System.Collections.Generic;

public static class Kata {
  public static IEnumerable<string> FriendOrFoe (string[] names) {
    return Array.FindAll( names, x => x.Length==4);
  }
}

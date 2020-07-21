class Kata {
    static def alphabetPosition(text) {
        def t = text.toLowerCase().replaceAll("[^A-Za-z]", "")
        def list =[]
        t.each {
          list<<(int)it-96
        }
        return list.join(" ")
    }
}

function DNAStrand(dna){
  const code = {A:"T", T:"A", C:"G", G:"C"}
  return dna.split("").map(l=>code[l]).join("")
}

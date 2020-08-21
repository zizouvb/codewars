String rnaToDna(String dna) {
  var output = "";
  dna.split("").forEach((item){
    if (item=="T"){
      output += "U";
    } else {
      output += item;
    }
  });
  return output;
}

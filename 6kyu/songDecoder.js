function songDecoder(song){
  return song.split(["WUB"]).join(" ").split(" ").filter(i=>i).join(" ")
}

String printerError(String s) {
  var errorsNb = s.split('').where((c) => c.codeUnitAt(0) > 'm'.codeUnitAt(0));
  return errorsNb.length.toString()+"/"+s.length.toString();
}

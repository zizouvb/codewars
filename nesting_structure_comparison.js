Array.prototype.sameStructureAs = function (other) {
  return this.length === other.length
    ? this.every((sub, i) => {
        return isArray(sub) ? sub.sameStructureAs(other[i]) : true;
      })
    : false;
};

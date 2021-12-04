function domainName(url) {
  let reg = /(http:\/\/|https:\/\/)?(www\.)?(.[^/.]+)/;
  return url.match(reg)[3];
}

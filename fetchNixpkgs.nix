{ rev    ? "5a25280e914de33e5dc3fb4e10b962dc571cfdf6"             # The Git revision of nixpkgs to fetch
, sha256 ? "0iasfh1jqw99zbzqsrcg7fj02gsk46nmama4gkp3jn85gndhrs00" # The SHA256 of the downloaded data
}:

builtins.fetchTarball {
  url = "https://github.com/airalab/airapkgs/archive/${rev}.tar.gz";
  inherit sha256;
}

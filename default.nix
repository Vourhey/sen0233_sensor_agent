{ stdenv
, mkRosPackage
, robonomics_comm
, python3Packages
}:

mkRosPackage rec {
  name = "${pname}-${version}";
  pname = "sensors_pack_agent";
  version = "0.2.0";

  src = ./.;

  propagatedBuildInputs = [
    robonomics_comm
    python3Packages.pyserial
  ];

  meta = with stdenv.lib; {
    description = "Agent that offers data from sensors";
    homepage = http://github.com/vourhey/sensors_pack_agent;
    license = licenses.bsd3;
    maintainers = with maintainers; [ vourhey ];
  };
}

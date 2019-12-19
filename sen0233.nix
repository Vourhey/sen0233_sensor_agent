{ config, lib, pkgs, ... }:

with lib;

let
  cfg = config.services.sen0233;
  varDir = "/var/lib/sen0233";

in {

  options = {
    services.sen0233 = {
      enable = mkEnableOption "Sensors pack service";

      package = mkOption {
        type = types.package;
        default = pkgs.sensors_pack_agent;
        defaultText = "pkgs.sensors_pack_agent";
        description = '' '';
      };

      user = mkOption {
        type = types.str;
        default = "liability";
        description = "User account under which substrate node robonomics runs";
      };

      group = mkOption {
        type = types.str;
        default = "users";
        description = "Group under which substrate node robonomics user";
      };
    };
  };

  config = mkIf cfg.enable {

    systemd.services.sen0233 = {
      requires = [ "ipfs.service"  "roscore.service" ];
      after = [ "ipfs.service" "roscore.target" ];
      wantedBy = [ "multi-user.target" ];
      serviceConfig = {
        Restart = "on-failure";
        RestartSec = 5;
        ExecStart = concatStringsSep " " [
          ''source ${cfg.package}/setup.bash &&''
          ''roslaunch sensors_pack_agent agent.launch''
        ];
        User = cfg.user;
        Group = cfg.group;
        UMask = "0007";
        WorkingDirectory = varDir;
      };
    };
  };
}

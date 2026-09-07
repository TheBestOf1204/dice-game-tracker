# shell.nix
let

  # We pin to a specific nixpkgs commit for reproducibility.

  # Last updated: 2024-04-29. Check for new commits at https://status.nixos.org.

  pkgs =
    import
      (fetchTarball "https://github.com/NixOS/nixpkgs/archive/bcd464ccd2a1a7cd09aa2f8d4ffba83b761b1d0e.tar.gz")
      { };
in
pkgs.mkShell {

  packages = [

    (pkgs.python3.withPackages (
      python-pkgs: with python-pkgs; [

        # select Python packages here

      ]
    ))

  ];
}

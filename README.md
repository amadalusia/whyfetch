### whyfetch? 🤔

###### a fetch script that makes you ask why

---

### why whyfetch?

As per tradition when making new dotfiles (as well as the reason why norshfetch and norfetch were archived)
I usually create my own fetch script to accompany it. In this case I created a new rice involving Rose Pine which means my other scripts are as such outdated.
Especially since they call Linux-only functions. which is abhorrently cringe looking back.

### installing (with nix)

You can install this program by running the following in your command line.

```shell
% nix profile install "github:amadalusia/whyfetch#whyfetch"
```

However if you want to install it to your NixOS configuration (particularly with the help of flakes), [you can consume the overlay provided by the flake.](https://wiki.nixos.org/wiki/Overlays#In_NixOS)

### installing

~~[Download Nix](https://nixos.org/download/) and then follow the instructions above.~~

If you want to install the program  then the following instructions below will get you there.
```shell
% poetry build
```

This will give you the `.whl` needed to run `pip install` on in the `dist/` directory.

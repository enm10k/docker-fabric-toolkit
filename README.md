# docker-fabric-toolkit

The following tools in a Docker container:

- Fabric
  - with rsync suppot
- Git
- Boto 3

```
$ git clone https://github.com/enm10k/docker-fabric-toolkit.git
$ cd docker-fabric-toolkit

# for macOS
$ echo 'alias fab='"'"'docker run --rm -it -v "$PWD:/app" -v "$HOME/.ssh:/root/.ssh" -v "$HOME/.aws:/root/.aws" enm10k/docker-fabric-toolkit fab'"'"'>>~/.bash_profile
$ source ~/.bash_profile

$ fab hello
[localhost] local: echo Hello World!
Hello World!
[localhost] local: git --version
git version 2.8.6
[localhost] local: rsync --version
rsync  version 3.1.3  protocol version 31
Copyright (C) 1996-2018 by Andrew Tridgell, Wayne Davison, and others.
Web site: http://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, hardlinks, symlinks, IPv6, batchfiles, inplace,
    append, ACLs, xattrs, iconv, symtimes, prealloc

rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
are welcome to redistribute it under certain conditions.  See the GNU
General Public Licence for details.
[localhost] local: python -c "import boto3; print(boto3.__version__)"
1.9.73

Done.
```

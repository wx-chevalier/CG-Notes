# Blender Examples

# 安装 Pip

First of all, pip is not part of Python so it doesn't come by default with Blender. It has to be installed for Blender's bundled Python even if you already have pip for some other version of Python on your system. For this get the get-pip.py file from the pip documentation

You'll find the blender python binary at:

```sh
/blender-path/2.xx/python/bin/python
```

Use this binary to run the get-pip.py. If you have it saved in your home directory the command to use should look something like this:

```sh
$ /path/to/blender/blender-path/2.xx/python/bin/python3 ~/get-pip.py
```

You should now have pip installed for blender. You use it with blenders python too and you have to point to the pip that was installed for blenders python. Both are in blenders folder tree and you use them like this:

```sh
$ /blender-path/2.xx/python/bin/python /blender-version/2.xx/python/local/lib/python3.5/dist-packages/pip install scipy
```

This installs scipy for your blenders python. Of course you have to adjust names according to the version you use, but it worked for me for 2.77.

I just tried to do this again and with a recent build I did not have to point to he installed pip, calling blenders python was enough, my command looked like:

```sh
/path/to/blenderspython/python pip install module
```

blender-2.8: pip is already included so the only step to do this for blender-2.8 is:

```sh
$ /path/to/blenderspython/pip install module
```

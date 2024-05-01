# AFRL Generator Cores
### Generators for various pre build needs
---

   author: Jay Convertino  
   
   date: 2022.08.09  
   
   details: Various generators for fusesoc cores, such as rom generators and software library handling.  
   
   license: MIT   
   
---

### Version
#### Current
  - V1.0.0 - initial release

#### Previous
  - none

### CORES
```
strromgen:
  interpreter: python3
  command: python/strromgen.py
  description: Generate ROMS based on YAML file containing strings and values.
  usage: |
    Bunch of cool stuff and such.

    Parameters:
      yaml_file   (str):  input file name to generate rom from in YAML format.
      rom_file    (str):  output rom file name for binary contents.
      endian      (str):  Endianess of integers.
      num_bytes   (int):  Number of bytes for integer values.
      string_size (int):  Number of characters for strings, including null terminator. All added characters will be null terminator.

gen_make:
  interpreter: python3
  command: python/gen_make.py
  description: Generate C libraries for VPI source code using make files.
  usage: |
    Bunch of cool stuff and such.

    Parameters:
      src_dir   (str): Directory containing the makefile execute.
      make_args (str): Make arguments

gen_cmake:
  interpreter: python3
  command: python/gen_cmake.py
  description: Generate C libraries for VPI source code using cmake files.
  usage: |
    Bunch of cool stuff and such.

    Parameters:
      src_dir  (str): Directories containing the cmake file for a library to build.
      build_dir(str): Where to build output products. This defaults to build.
      cmake_args(str): Arguments added to cmake build.

spinalhdl:
  interpreter: python3
  command: python/spinalhdl.py
  description: Generate verilog files from spinalhdl source with sbt command
  usage: |
    Requires JRE v17 install. If local must be used please set JAVA_HOME environment variable.

    Parameters:
      src_dir  (str): Directories containing the sbt file for the ip.
      sbt_tgz_archive_url(str): URL of to a tar gz compressed archive of the sbt tool. Will auto install and use
      build_args(str): list of command line arguments to pass to sbt.

git_pull:
  interpreter: python3
  command: python/git_pull.py
  description: Pull git repos
  usage: |
    Pull git repos and place them in a particular directory.

    Python Dependencies:
    - PyYAML
    - GitPython

    Parameters:
      repo_url (str): URL where the git repo resides.
      repo_dir (str): folder to put the pull.
      tag (str): optional, tag to checkout from pull.
      patch (str): optional, file to patch repo (last step).
```

##### Dependencies
  - PyYAML : python3
  - GitPython : python3
  - Java17 : native


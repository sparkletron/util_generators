# AFRL Fusesoc Generator Cores
### Generators for various pre build needs

![image](img/AFRL.png)

---

   author: Jay Convertino  
   
   date: 2022.08.09  
   
   details: Various generators for fusesoc cores, such as rom generators and software library handling.  
   
   license: MIT   
   
---

### VERSION
#### Current
  - V1.0.0 - initial release

#### Previous
  - none

### DEPENDENCIES
  - PyYAML : python3
  - GitPython : python3
  - Java17 : native

### CORES
- strromgen: Generate ROMS based on YAML file containing strings and values.

- gen_make: Generate C libraries for VPI source code using make files.


- gen_cmake: Generate C libraries for VPI source code using cmake files.

- spinalhdl: Generate verilog files from spinalhdl source with sbt command

- git_pull: Pull git repos

### FUSESOC
The following is how to use the generators in a core file, and example parameter usage for each generator.

- Usage in a core file.

```
filesets:
  dep_gen:
    depend:
      - AFRL:utility:generators:1.0.0

generate:
  gen_git:
    generator: git_pull
    parameters:
      repo_url: https://github.com/sparkletron/C89_pthread_ring_buffer.git
      repo_dir: lib_ringbuffer
      tag: release_v1.6.1
  gen_lib:
    generator: gen_cmake
    parameters:
      src_dir:  lib_ringbuffer
      cmake_args: ["-DCMAKE_POSITION_INDEPENDENT_CODE=ON"]

targets:
  default: &default
    description: default target
    filesets: [dep_gen]
    generate: [gen_git, gen_lib]
```

- git_pull

```
filesets:
  dep:
    depend:
      - AFRL:utility:generators:1.0.0

generate:
  gen_git:
    generator: git_pull
    parameters:
      repo_url: https://github.com/SpinalHDL/SpinalHDL.git
      repo_dir: SpinalHDL
      tag: v1.10.1
```

- gen_cmake

```
filesets:
  dep:
    depend:
      - AFRL:utility:generators:1.0.0

generate:
  gen_lib:
    generator: gen_cmake
    parameters:
      src_dir:  lib_ringbuffer
      cmake_args: ["-DCMAKE_POSITION_INDEPENDENT_CODE=ON"]
```

- gen_make

```
filesets:
  dep_gen:
    depend:
      - AFRL:utility:generators:0.0.0

generate:
  gen:
    generator: gen_make
    parameters:
      src_dirs:  [lib/C89_pthread_ring_buffer]
```

- spinalhdl

```
filesets:
  dep:
    depend:
      - AFRL:utility:generators:1.0.0

generate:
  gen_spinalHDL:
    generator: spinalhdl
    parameters:
      src_dir: cores/veronica
      build_args: ["runMain", "vexriscv.afrl.Veronica_Axi"]
```

- strromgen

```
filesets:
  dep:
    depend:
      - AFRL:utility:generators:0.0.0

generate:
  gen_rom:
    generator: strromgen
    parameters:
      yaml_file:  gen/rom.yml
      rom_file: gen/strings.rom
      endian:  little
```


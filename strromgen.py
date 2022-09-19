#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import yaml

class strromgen(Generator):
    def run(self):
      #open files
      yaml_file   = self.config.get('yaml_file')
      rom_file    = self.config.get('rom_file')
      endian      = self.config.get('endian', 'little')
      num_bytes   = self.config.get('num_bytes', 4)
      
      #open yaml file
      try:
        yaml_fileD = open(self.files_root + '/' + yaml_file, 'r')
      except Exception as ex:
        print(ex)
        exit(1)      
      
      #open output rom file for binary writing
      try:
        rom_fileD = open(self.files_root + '/' + rom_file, 'wb')
      except Exception as ex:
        print(ex)
        exit(1)
        
      try:
        yaml_load = yaml.safe_load(yaml_fileD)
      except Exception as ex:
        print(ex)
      
      #check for the header key
      key_dict = yaml_load.get('rom_strings')
      
      if(key_dict is None):
        print("ERROR: Starting key value for list must be \"rom_stings\"")
        exit(1)
      
      # extract, write and output each key and value
      # write key and value to a rom file
      for key, value in key_dict.items():
          rom_fileD.write(bytearray(key, 'utf8'))
          rom_fileD.write((value).to_bytes(num_bytes, endian))
      
      rom_fileD.close()
      yaml_fileD.close()
      
g = strromgen()
g.run()
g.write()

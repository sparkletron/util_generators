#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import yaml

################################################################################
## strromgen
# @file   strromgen.py
# @author Jay Convertino(johnathan.convertino.1@us.af.mil)
# @date   23.01.01
# @brief  Generate rom with string lookup to binary integer value.
#
# @license MIT
# Copyright 2023 Jay Convertino
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
################################################################################
class strromgen(Generator):
    def run(self):
      #open files
      yaml_file   = self.config.get('yaml_file')
      rom_file    = self.config.get('rom_file')
      endian      = self.config.get('endian', 'little')
      num_bytes   = self.config.get('num_bytes', 4)
      string_size = self.config.get('string_size', 16)
      
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
      # write key, null, and then a value to a rom file
      for key, value in key_dict.items():
          rom_fileD.write(bytearray(key, 'utf8'))
          rom_fileD.write((string_size - len(key)) * ('\n'.encode()))
          rom_fileD.write((value).to_bytes(num_bytes, endian))
      
      rom_fileD.close()
      yaml_fileD.close()
      
g = strromgen()
g.run()
g.write()

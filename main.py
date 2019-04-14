from LZW import LZW
import os

compressor = LZW(os.path.join("Images","small.tif"))
compressor.compress()

decompressor = LZW(os.path.join("CompressedFiles","smallCompressed.lzw"))
decompressor.decompress()
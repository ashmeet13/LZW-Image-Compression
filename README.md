# LZW-Image-Compression
An attempt to implement the famous compression algorithm by Lempel-Ziv-Welch. This is not a perfect implementation of the algorithim as it does not perform up to the mark. For further details go to **Further Improvements Section**

## To Run  
-  Save the LZW.py file  
-  Use ``` from LZW import LZW ```  
-  For compression:  
    * ```compressor = LZW('''Path to Image''')```  
    * ```compressor.compress()```  
-  For decompression:  
    * ```decompressor = LZW('''Path to LZW File''')```  
    * ```decompressor.decompress()```  
    
## Further Improvements
-  As of now, the compression only works for 8-Bit Images with TIFF format.
-  The decompressed image sometimes explodes in size than what it originally was before being compressed.
-  A UI to be integrated.

# FlatBuffer_Assignment

1: cd encoder_in_python

2: ..\flatc.exe -p -b ..\schema.fbs

3: python fb_encoder.py

4: cd decoder_in_cpp

5: ..\flatc.exe -c -b ..\schema.fbs 

6: g++ -I ../ fb_decoder.cpp -o fb_decoder.exe

7: fb_decoder.exe
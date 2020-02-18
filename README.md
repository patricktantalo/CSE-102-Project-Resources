# Project Resources


### Files for CSE 102-01 (Winter 2020)
- Check - verifies input_file output_file pair for this project
- in1 - input file
- in2 - input file
- in3 - input file
- in4 - input tile
- out1 - output file corresponding to in1
- out2 - output file corresponding to in2
- out3 - output file corresponding to in3
- out4.1, out4.2, out4.3, out4.4, out4.5, out4.6 - output files all corresponding to in4
- README.md - this file


### Notes
Check is a Linux binary executable file. Make it excutable by typing at the command prompt: 

```sh
chmod 700 Check
```
then run it by typing:

```sh
Check input_file output_file
```

If output_file is valid for input_file, there will be no ouput. If output_file is invalid for input_file, an error message will be printed giving at least one reason for the mismatch. It is not guaranteed that all errors in output_file will be reported.

Observe that file in4 represents a connected graph with 6 different minimum weight spanning trees, represented by files out4.1 through out4.6. 

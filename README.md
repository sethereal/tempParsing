
## Libraries Required

The following libraries are required to run this code:

- `sys`
- `os`
- `numpy`
- `parse_temps`
- `pieceInterpret`
- `leastSquaresApproximation`

## Compilation Instructions

This code does not require a build file (interpreted language python ftw)

## How to Run

To run this code, follow these steps:

1. Open a terminal.
2. Navigate to the directory containing the `driver.py` file.
3. Run the following command: 

    ```
    python driver.py <input_temps_file_path>
    ```

Replace `<input_temps_file_path>` with the path to your input temperatures file.

## Output

The output will be written to four files in the current directory, one for each core. 
The interpolation files will be named `core1_output.txt`, `core2_output.txt`, `core3_output.txt`, and `core4_output.txt`. 
The LSA files will be named `core1_lsa_output.txt`, `core2_lsa_output.txt`, `core3_lsa_output.txt`, and `core4_lsa_output.txt`. 
Each file will contain the interpolated/LSA temperature data for the corresponding core.
Do note that if it is not preferred to have another four separate files just for least squares approximation,
you can replace `_lsa_output.txt` with  `_output.txt` on line 46, and each LSA will be at the bottom of the corresponding files.


## Sample Output Listing
```
	   0 <= x <=       30 ; y =      61.0000 +       0.6333 x ; interpolation
      30 <= x <=       60 ; y =      98.0000 +      -0.6000 x ; interpolation
      60 <= x <=       90 ; y =      20.0000 +       0.7000 x ; interpolation
      90 <= x <=      120 ; y =     128.0000 +      -0.5000 x ; interpolation
       0 <= x <=      120 ; y =      67.4000 +       0.0567 x ; least-squares
```

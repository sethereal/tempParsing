import sys
from parse_temps import parse_raw_temps
from leastSquaresApproximation import lsaMethod
from pieceInterpret import linear_interpolation


def main():
    

    """
    This is the driver function:
    It reads temperature data from an input file, processes it, and produces output files with interpolated data
    for each of the four cores. The interpolation is performed between data points to estimate temperature values.

    :return: None
    """
	
    input_temps = sys.argv[1]


    with open(input_temps, 'r') as temps_file:
        times = []
        core_data = [[] for _ in range(0, 4)]

        for time, raw_core_data in parse_raw_temps(temps_file):
            times.append(time)
            for core_idx, reading in enumerate(raw_core_data):
                core_data[core_idx].append(reading)


    for core_idx in range(4):
        core_temps = core_data[core_idx]


        #Linear Interpolation
        interpolated_data = linear_interpolation(times, core_temps)

        #LSA 
        lsa_interpolated_data = lsaMethod(core_temps)
        
        output_file_name = f"core{core_idx + 1}_output.txt"
        with open(output_file_name, 'w') as output_file:
            for x_min, x_max, a, b in interpolated_data:
                output_file.write(f"{x_min} <= x <= {x_max} ; y = {a:.4f} + {b:.4f} x ; interpolation\n")

        output_file_name = f"core{core_idx + 1}_lsa_output.txt"
        with open(output_file_name, 'w') as output_file:
            x_min, x_max, c, d = lsa_interpolated_data
            output_file.write(f"{x_min} <= x <= {x_max} ; y = {c:.4f} + {d:.4f} x ; least-squares\n")


if __name__ == "__main__":

    main()

import subprocess
from argparse import ArgumentParser
import os
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('input_path', type=str)
    parser.add_argument('style_image_path', type=str)
    parser.add_argument('output_path', type=str)
    args = parser.parse_args()

    if not os.path.exists(args.output_path): 
        os.makedirs(args.output_path) 
    input_file_names = os.listdir(args.input_path)
    input_file_paths = [os.path.join(args.input_path, name) for name in input_file_names]
    output_file_paths = [os.path.join(args.output_path, name) for name in input_file_names]
    for i,o in zip(input_file_paths, output_file_paths):
        completed_process = subprocess.run(["style_transfer", i, args.style_image_path, "-o", o, "--end-scale", "1024", "--iterations", "150", "--initial-iterations", "150", "--content-weight", "0.1"])

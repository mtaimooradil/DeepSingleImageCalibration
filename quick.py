from calib.demo import DeepCalibration
from pathlib import Path
import argparse
import pickle

parser = argparse.ArgumentParser(description='Get calibration parameters from an image.')
parser.add_argument('--image_path', type=str, required = True, help='The path to the input image')
parser.add_argument('--save_path', type=str, required = True, help='The path where the image should be saved')

args = parser.parse_args()

# image_path = r'E:\PhD Work (Local)\ML\Calibration\DeepSingleImageCalibration\images\img201.png'
# save_path = r'E:\PhD Work (Local)\ML\Calibration\DeepSingleImageCalibration\calib_params2.pkl'

calib = DeepCalibration()
params = calib.calibrate_from_path(Path(args.image_path))

with open(Path(args.save_path), 'wb') as f:
    pickle.dump(params, f)

print(params)
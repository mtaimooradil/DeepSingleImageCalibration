from calib.demo import DeepCalibration

image_path = r'E:\PhD Work (Local)\ML\Calibration\DeepSingleImageCalibration\images\img201.png'

calib = DeepCalibration()
params = calib.calibrate_from_path(image_path)
print(params)
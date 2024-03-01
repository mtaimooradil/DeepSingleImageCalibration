from calib.demo import DeepCalibration


def calibrator(**kwargs):
    return DeepCalibration(**kwargs)


dependencies = ['pycolmap', 'torch', 'cv2', 'numpy']

# tu_lmk_reg_test_mat_to_json.py
# Script to extract coordinates (and 
# confidence values) estimated by 
# Tango Unchained (TU) landmark (lmk) 
# regression (reg) model on test dataset
# from MAT files to JSON files

# Author: Matthieu Ruthven (matthieu.ruthven@uni.lu)
# Last modified: 3rd January 2024

# Import required modules
import argparse
import os
from pathlib import Path
from scipy.io import loadmat
import numpy as np
import json

# Main function
def main(filepath):

    # Determine test dataset
    if 'lightbox' in str(filepath.parent):
        test_dset = 'Lightbox'
        n_img = 6740
    elif 'sunlamp' in str(filepath.parent):
        test_dset = 'Sunlamp'
        n_img = 2791

    # Load MAT file of landmark coordinates and confidence values
    lmk_coords = loadmat(filepath)
    lmk_coords = lmk_coords['preds']

    # Check consistent number of coordinates
    assert lmk_coords.shape[0] == n_img, 'Inconsistent number of accuracy values'

    # Check x-coordinates
    assert not np.any(lmk_coords[..., 0] < -1920) and not np.any(lmk_coords[..., 0] > 2 * 1920),'Inconsistent x-coordinate value(s)'
    print(f'x-coordinate: min={np.min(lmk_coords[..., 0])} max={np.max(lmk_coords[..., 0])}')

    # Check y-coordinates
    assert not np.any(lmk_coords[..., 1] < -1200) and not np.any(lmk_coords[..., 1] > 2 * 1200),'Inconsistent y-coordinate value(s)'
    print(f'y-coordinate: min={np.min(lmk_coords[..., 1])} max={np.max(lmk_coords[..., 1])}')

    # Check confidence values
    # assert not np.any(lmk_coords[..., -1] < 0) and not np.any(lmk_coords[..., -1] > 1),'Inconsistent confidence value(s)'
    print(f'Confidence value: min={np.min(lmk_coords[..., -1])} max={np.max(lmk_coords[..., -1])}')
    
    # Create JSON file of coordinates
    dict_list = []
    for idx in range(n_img):
        tmp_lmk_coords = np.reshape(lmk_coords[idx, ...], -1).tolist()
        dict_list.append({'filename': f'img{(idx+1):06}.jpg', 
                          'keypoints': tmp_lmk_coords})
    
    # Path to where JSON file will be saved
    filepath = filepath.parent / f'{test_dset.lower()}_test.json'

    # Save file
    with open(filepath, 'w') as outfile:
        json.dump(dict_list, outfile, indent=3)

if __name__ == '__main__':

    # Create parser
    parser = argparse.ArgumentParser(description='Extract accuracy values from MAT file')

    # Add arguments
    parser.add_argument('--filepath',
                        help='Path to log file',
                        required=True,
                        type=Path)

    # Parse arguments
    args = parser.parse_args()

    # Check file exists
    assert os.path.exists(args.filepath), f'There is no file {args.filepath.name} at path {args.filepath.parent}'

    # Run 
    main(args.filepath)
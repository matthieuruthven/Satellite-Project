# tu_lmk_reg_log_analysis.py
# Script to extract loss and accuracy values
# from log files during Tango Unchained (TU)
# landmark (lmk) regression (reg) training

# Author: Matthieu Ruthven (matthieu.ruthven@uni.lu)
# Last modified: 28th December 2023

# Import required modules
import argparse
import os
from pathlib import Path
import datetime
import pandas as pd


# Main function
def main(filepath):

    # Determine test dataset
    if 'lit' in filepath.stem:
        test_dset = 'Lightbox'
        indicator = 'Test: [200/211]'
    elif 'sun' in filepath.stem:
        test_dset = 'Sunlamp'
        indicator = 'Test: [0/88]'
    
    # If CSV file already created
    if os.path.exists(f'{filepath.parent}/{filepath.stem}.csv'):

        # Print update
        print(f'CSV file already created')

        # Load CSV file
        df = pd.read_csv('lightbox_model/PEdataset/hrnet_cms/lit_hpc_001/lit_hpc_001_2023-12-20-11-01_train.csv')

        # Add column
        df['TestDataset'] = 'Lightbox'

        # Load CSV file
        tmp_df = pd.read_csv(f'lightbox_model/PEdataset/hrnet_cms/lit_hpc_001/lit_hpc_001_2023-12-15-09-31_train.csv')

        # Add column
        tmp_df['TestDataset'] = 'Lightbox'

        # Combine CSV files
        df = pd.concat([tmp_df, df])

        # Load CSV file
        tmp_df = pd.read_csv('sunlamp_model/PEdataset/hrnet_cms/sun_hpc_001/sun_hpc_001_2023-12-18-18-11_train.csv')

        # Add column
        tmp_df['TestDataset'] = 'Sunlamp'

        # Combine CSV files
        df = pd.concat([tmp_df, df])

        # Load CSV file
        tmp_df = pd.read_csv(f'sunlamp_model/PEdataset/hrnet_cms/sun_hpc_001/sun_hpc_001_2023-12-13-20-46_train.csv')

        # Add column
        tmp_df['TestDataset'] = 'Sunlamp'

        # Combine CSV files
        df = pd.concat([tmp_df, df])

        # Load CSV file
        tmp_df = pd.read_csv(f'sunlamp_model/PEdataset/hrnet_cms/sun_hpc_001/sun_hpc_001_2023-12-13-10-43_train.csv')

        # Add column
        tmp_df['TestDataset'] = 'Sunlamp'
        
        # Combine CSV files
        df = pd.concat([tmp_df, df])

        # Save combined CSV files
        df.to_csv(f'TU_training_{datetime.date.today()}.csv', index=False)

    else:

        # Print update
        print('Create CSV file')

        # Lists for pandas DataFrame
        date_time_df = []
        domain_df = []
        dset_df = []
        epoch_df = []
        instance_df = []
        accuracy_df = []

        # Epoch counter
        prev_epoch = 0

        # Read log file
        with open(filepath) as f:
            
            for line in f:

                if 'Accuracy' in line:

                    if 'Epoch' in line:

                        # Extract date and time and update date_time_df
                        date_time_df.append(datetime.datetime.fromisoformat(line[:19]))

                        # Update domain_df
                        domain_df.append('Synthetic')

                        # Update dset_df
                        dset_df.append('Training')

                        # Extract epoch and update epoch_df
                        epoch = line.split('[')
                        epoch = int(epoch[1][:-1]) + 1
                        epoch_df.append(epoch)
                        if prev_epoch != epoch:

                            # Create prev_instance
                            prev_instance = 0

                        else:

                            # Update prev_instance
                            prev_instance += 1

                        # Update instance_df
                        instance_df.append(prev_instance)

                        # Update prev_epoch
                        prev_epoch = epoch

                        # Extract accuracy and update accuracy_df
                        accuracy = line.split('(')
                        accuracy = accuracy[-1]
                        accuracy = accuracy.split(')')
                        accuracy = float(accuracy[0])
                        accuracy_df.append(accuracy)

                    elif 'Test: [300/375]' in line:

                        # Extract date and time and update date_time_df
                        date_time_df.append(datetime.datetime.fromisoformat(line[:19]))

                        # Update domain_df
                        domain_df.append('Synthetic')

                        # Update dset_df
                        dset_df.append('Validation')

                        # Update epoch_df, instance and instance_df
                        epoch_df.append(epoch)
                        instance = 0
                        instance_df.append(instance)

                        # Extract accuracy and update accuracy_df
                        accuracy = line.split('(')
                        accuracy = accuracy[-1]
                        accuracy = accuracy.split(')')
                        accuracy = float(accuracy[0])
                        accuracy_df.append(accuracy)

                    elif indicator in line:

                        # Extract date and time and update date_time_df
                        date_time_df.append(datetime.datetime.fromisoformat(line[:19]))

                        # Update domain_df
                        domain_df.append(test_dset)
                        
                        # Update dset_df
                        dset_df.append('Test')

                        # Update epoch_df, instance and instance_df
                        epoch_df.append(epoch)
                        instance = 0
                        instance_df.append(instance)

                        # Extract accuracy and update accuracy_df
                        accuracy = line.split('(')
                        accuracy = accuracy[-1]
                        accuracy = accuracy.split(')')
                        accuracy = float(accuracy[0])
                        accuracy_df.append(accuracy)
        
        # Create pandas DataFrame
        df = pd.DataFrame({'Datetime': date_time_df,
                        'Domain': domain_df,
                        'Dataset': dset_df,
                        'Epoch': epoch_df,
                        'Instance': instance_df,
                        'Accuracy': accuracy_df})
        
        if filepath.stem == 'sun_hpc_001_2023-12-13-10-43_train':
            
            # Remove incomplete epochs
            df = df[df['Epoch'] <= 5]

        elif filepath.stem == 'sun_hpc_001_2023-12-13-20-46_train':

            # Remove incomplete epochs
            df = df[df['Epoch'] <= 21]

        elif filepath.stem == 'sun_hpc_001_2023-12-18-18-11_train':

            # Remove incomplete epochs
            df = df[df['Epoch'] <= 47]

        elif filepath.stem == 'lit_hpc_001_2023-12-15-09-31_train':

            # Remove incomplete epochs
            df = df[df['Epoch'] <= 26]

        elif filepath.stem == 'lit_hpc_001_2023-12-20-11-01_train':

            # Remove incomplete epochs
            df = df[df['Epoch'] <= 52]

        # Extract rows corresponding to training dataset only
        tmp_df = df[df['Dataset'] == 'Training']

        # Calculate position of instance within epoch
        tmp_df['position_within_epoch'] = tmp_df.groupby('Epoch').cumcount()

        # Calculate number of iterations in each epoch
        tmp_df['instances_per_epoch'] = tmp_df.groupby('Epoch')['Epoch'].transform('size')

        # Calculate instance ID
        tmp_df['InstanceID'] = tmp_df['Epoch'] + tmp_df['position_within_epoch'] / tmp_df['instances_per_epoch']

        # Add instance ID to df
        df['InstanceID'] = df['Epoch']
        df = df[df['Dataset'] != 'Training']
        df = pd.concat([df, tmp_df])

        # Save df
        df[['Datetime', 'Domain', 'Dataset', 'Epoch', 'InstanceID', 'Accuracy']].to_csv(f'{filepath.parent}/{filepath.stem}.csv', index=False)


if __name__ == '__main__':

    # Create parser
    parser = argparse.ArgumentParser(description='Extract loss and accuracy values from log files')

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
# Project creation
import deeplabcut

# Create project
deeplabcut.create_new_project(
    '{{ProjectName}}',
    '{{UserID}}',
    [
        # List of video file paths
    ],
    working_directory='./,
    copy_videos=False)

config_path = '{{ProjectFolder}}/config.yaml'

# Extract dataset frames for labeling with kmeans clustering
deeplabcut.extract_frames(config_path, 'automatic', 'kmeans',  userfeedback=False, crop=False)

# Open frame labeling tool
deeplabcut.label_frames(config_path)

# Add new videos to project
deeplabcut.add_new_videos(config_path,
    [
    # List of video file paths
    ]
    ,copy_videos=False)
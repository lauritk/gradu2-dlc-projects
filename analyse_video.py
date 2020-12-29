# Example for analysing videos with the trained model
import deeplabcut

# Path to project of the model
config_path = './959-18-training/config.yaml'

deeplabcut.analyze_videos(config_path,['./TIM18SDM018_ACAC_1_alkuosa.avi'],
    shuffle=1, save_as_csv=True)

# Extra
#deeplabcut.create_labeled_video(config_path, ['./TIM18SDM018_ACAC_1_alkuosa.avi'])
#deeplabcut.plot_trajectories(config_path, ['./TIM18SDM018_ACAC_1_alkuosa.avi'])
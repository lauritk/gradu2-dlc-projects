import deeplabcut

val_config_path = '/home/pop/GitHub/Gradu-2-0-deeplabconfig/256-3-validation/config.yaml'
train_config_path = '/home/pop/GitHub/Gradu-2-0-deeplabconfig/959-18-training/config.yaml'

# Train with the training data
deeplabcut.train_network(train_config_path, shuffle=1, max_snapshots_to_keep=150, maxiters=930000)

# Evaluate data with the trained model
deeplabcut.evaluate_network(val_config_path, plotting = False, trainingsetindex='all')
deeplabcut.evaluate_network(train_config_path, plotting = False, trainingsetindex='all')
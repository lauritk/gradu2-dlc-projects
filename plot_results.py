# Plots overall bodypart detection results
import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = [16, 9]

# Run train and(or) evaluation first to get results!

learning_data = pd.read_csv('./959-18-training/dlc-models/iteration-0/of-rodent-tracking-959-18-single-passMay3-trainset95shuffle1/train/learning_stats.csv', names=['Iterations', 'Loss', 'Learning rate'])
training_eval = pd.read_csv('./959-18-training/evaluation-results/iteration-0/of-rodent-tracking-959-18-single-passMay3-trainset95shuffle1/DLC_resnet50_of-rodent-tracking-959-18-single-passMay3shuffle1_930000-results.csv')
novel_eval = pd.read_csv('./256-3-validation/evaluation-results/iteration-0/of-rodent-tracking-256-3-validationMay3-trainset100shuffle1/DLC_resnet50_of-rodent-tracking-256-3-validationMay3shuffle1_930000-results.csv')

# Plot
fig, ax = plt.subplots()
ax.set_xlabel("Iterations")
ax.set_ylim([0, 0.035])

ax.plot(learning_data['Iterations'], learning_data['Loss'], color='blue')
ax.plot(learning_data['Iterations'], learning_data['Learning rate'], color='red')
ax.set_ylabel("Loss & learning rate")

ax2=ax.twinx()
ax2.set_ylim([0, 55])
ax2.plot(training_eval['Training iterations:'], training_eval[' Train error(px)'], color='green')
ax2.plot(training_eval['Training iterations:'], training_eval[' Test error(px)'], color='orange')
ax2.plot(novel_eval['Training iterations:'], novel_eval[' Train error(px)'], color='purple', label='Novel set error(px)')
ax2.plot(novel_eval['Training iterations:'], novel_eval['Train error with p-cutoff'], color='black', label='Novel set error(px) confidence > 0.6')
ax2.set_ylabel("Validation error (px)")

ax.legend(loc="upper center")
ax2.legend(loc="upper right")
fname = 'default-dataset'
plt.savefig('./' + fname + '.png', dpi=300, facecolor='w', edgecolor='w',
        orientation='landscape', format='png', pad_inches=0.1)
plt.savefig('./' + fname + '.svg', dpi=300, facecolor='w', edgecolor='w',
        orientation='landscape', format='svg', pad_inches=0.1)
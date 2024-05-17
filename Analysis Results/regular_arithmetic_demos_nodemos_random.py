import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
import numpy as np

# Data
models = [
    'Mamba-2.8b', 'Cerebras-btlm-3b', 'Mamba-7b',
    'Llama2-7b', 'Mistral-7b'
]

no_demos = [42, 18, 43, 37, 80]
demos_true_label = [64, 23, 65, 40, 88]
demos_random_label = [64, 24, 66, 44, 64]

x = np.arange(len(models))  # The label locations
width = 0.2  # The width of the bars

fig, ax = plt.subplots(figsize=(12, 4))

rects1 = ax.bar(x - width, no_demos, width, label='No Demos', color='#8ecae6')
rects2 = ax.bar(x, demos_true_label, width, label='Demos w/ True Label', color='#fb8500')
rects3 = ax.bar(x + width, demos_random_label, width, label='Demos w/ Random Label', color='#023047')

# ax.set_xlabel('Models')
ax.set_ylabel('Accuracy (%)')
ax.set_title('Accuracy of Regular Arithmetic Problems with Different Numbers of Demonstration')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
plt.ylim(0, 100)

plt.savefig('regular_arithmetic_demos_nodemos_random.png')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data
models = [
    'Mamba-2.8b', 'Cerebras-btlm-3b', 'Mamba-7b',
    'Llama2-7b', 'Mistral-7b'
]

demos_true_label = [76.81, 51.43, 66.3, 64.46, 91.85]
demos_true_label_with_cot = [50.16, 58.0, 62.27, 74.42, 89.56]
no_demos = [46.36, 21.42, 52.94, 27.7, 56.92]
demos_random_label = [56.12, 56.41, 59.35, 52.93, 89.37]


x = np.arange(len(models))
width = 0.2

fig, ax = plt.subplots(figsize=(12, 4))

rects1 = ax.bar(x - 1.5 * width, no_demos, width, label='No Demos', color='#8ecae6')
rects2 = ax.bar(x - 0.5 * width, demos_true_label, width, label='Demos w/ True Label', color='#fb8500')
rects3 = ax.bar(x + 0.5 * width, demos_random_label, width, label='Demos w/ Random Label', color='#023047')
rects4 = ax.bar(x + 1.5 * width, demos_true_label_with_cot, width, label='Demos w/ CoT Prompting', color='#ffb703')

# ax.set_xlabel('Models')
ax.set_ylabel('Macro-F1 (%)')
ax.set_title('Macro-F1 of Sentiment Analysis Problems with Different Demonstrations')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()
plt.ylim(0, 100)

plt.savefig('sentiment_demos_nodemos_random_cot.png')

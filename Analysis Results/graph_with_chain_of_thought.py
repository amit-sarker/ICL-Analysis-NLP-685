import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
import numpy as np

# Data for chain of thought with 3 demonstrations
chain_of_thought = {
    'Mamba-2.8b': 6,
    'Cerebras-btlm-3b': 8,
    'Mamba-7b': 18,
    'Llama2-7b': 16,
    'Mistral-7b': 66
}

colors = ['#8ecae6', '#219ebc', '#023047', '#ffb703', '#fb8500']

# First plot: Accuracy with Chain of Thought
models = list(chain_of_thought.keys())
cot_accuracy = list(chain_of_thought.values())
x = np.arange(len(models)) * 0.5  # The label locations

fig1, ax1 = plt.subplots(figsize=(8, 4))

# Plot bar chart for chain of thought accuracy
ax1.bar(x, cot_accuracy, width=0.3, color=colors, align='center')

# Adding titles and labels
# ax1.set_xlabel('Models')
ax1.set_ylabel('Accuracy (%)')
ax1.set_title('Model Accuracy with Chain of Thought (3 demos)')
ax1.set_xticks(x)
ax1.set_xticklabels(models)

# Adding accuracy values on top of the bars
for i in range(len(models)):
    ax1.text(x[i], cot_accuracy[i] + 1, f'{cot_accuracy[i]}%', ha='center', va='bottom')

# Show grid
ax1.grid(False)

# Save the first plot
plt.tight_layout()
plt.savefig('model_accuracy_chain_of_thought.png')
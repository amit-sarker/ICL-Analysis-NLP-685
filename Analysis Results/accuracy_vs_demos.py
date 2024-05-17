import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

demonstrations = [2, 4, 6, 8, 10]

mamba_28b = [8, 2, 8, 2, 4]
cerebras_btlm_3b = [0, 0, 0, 0, 0]
mamba_7b = [2, 4, 4, 6, 2]
llama2_7b = [18, 32, 24, 14, 32]
mistral_7b = [40, 48, 62, 50, 68]

plt.figure(figsize=(10, 6))

plt.plot(demonstrations, mamba_28b, marker='o', label='Mamba-2.8b', color='#8ecae6')
plt.plot(demonstrations, cerebras_btlm_3b, marker='o', label='Cerebras-btlm-3b', color='#219ebc')
plt.plot(demonstrations, mamba_7b, marker='o', label='Mamba-7b', color='#023047')
plt.plot(demonstrations, llama2_7b, marker='o', label='Llama2-7b', color='#ffb703')
plt.plot(demonstrations, mistral_7b, marker='o', label='Mistral-7b', color='#fb8500')

plt.title('Model Accuracy with Different Numbers of Demonstrations')
plt.xlabel('Number of Demonstrations')
plt.ylabel('Accuracy (%)')
plt.legend()

plt.grid(False)
plt.savefig('accuracy_vs_demos_jumbled_arithmetic.png')

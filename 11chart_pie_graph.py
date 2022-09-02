import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Ruby', 'Java'

sizes = [215, 130, 245, 210]

plt.pie(sizes,labels=labels)

plt.title('Language in use')

plt.show()
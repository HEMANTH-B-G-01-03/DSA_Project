import matplotlib.pyplot as plt 
n = [10, 50, 100, 1000, 5000, 10000]
linear_time = [0.00001460, 0.00001120, 0.00001010, 0.00004660, 0.00020130, 0.00051130]
hybrid_time = [0.00001110, 0.00001060, 0.00000700, 0.00001100, 0.00001150, 0.00001160]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(n, linear_time, marker='o', label='Linear Search')
plt.plot(n, hybrid_time, marker='s', label='Interpolation + Linear Search')

plt.xlabel("Total Number of Elements (n)")
plt.ylabel("Time (seconds)")
plt.title("Performance Comparison of Search Algorithms")
plt.legend()
plt.grid(True)

# Save graph as JPG
plt.savefig("search_comparison_graph.jpg", dpi=300, bbox_inches='tight')
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import ast

# Read the data from an external CSV file
file_path = 'FirstGame.csv'
df = pd.read_csv(file_path)

# Extract mouse positions as tuples from the 'MOUSE_POSITION' column
df['MOUSE_POSITION'] = df['MOUSE_POSITION'].apply(ast.literal_eval)

# Plot the points
# plt.scatter(df['MOUSE_POSITION'].apply(lambda x: x[0]), df['MOUSE_POSITION'].apply(lambda x: x[1]), label='Mouse Position', s=1)
plt.scatter(df['MOUSE_POSITION'].str[0], df['MOUSE_POSITION'].str[1], label='Mouse Position', s=1)

plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Mouse Positions over Time')
plt.legend()
plt.show()

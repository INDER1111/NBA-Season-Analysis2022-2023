
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (adjust file path)
df = pd.read_csv('nba_2022_2023_season.csv')

# Check the first few rows of the dataset
print(df.head())

# Handle missing values (if any)
df.dropna(inplace=True)

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Summary of dataset
print(df.describe())

# Calculate league averages
league_averages = df[['Points', 'Assists', 'Rebounds', 'FieldGoal%', '3Point%', 'FreeThrow%', 'Turnovers']].mean()
print("League Averages:\n", league_averages)

# Team-level analysis
team_stats = df.groupby('Team').mean()

# Display top-performing teams by points per game
top_teams_ppg = team_stats[['Points']].sort_values(by='Points', ascending=False)
print(top_teams_ppg.head())

# Plot top teams by PPG
plt.figure(figsize=(12, 6))
sns.barplot(x=top_teams_ppg.index, y=top_teams_ppg['Points'], palette='coolwarm')
plt.title('Top Teams by Points per Game (PPG) - 2022-2023 NBA Season')
plt.xticks(rotation=90)
plt.ylabel('Points per Game')
plt.show()

# Filter top players by PER
top_players_per = df.groupby('Player')['PER'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_players_per.index, y=top_players_per, palette='viridis')
plt.title('Top 10 Players by PER - 2022-2023 NBA Season')
plt.xticks(rotation=45)
plt.ylabel('Player Efficiency Rating (PER)')
plt.show()

# Scatter plot of 3P% vs. Points
plt.figure(figsize=(10,6))
sns.scatterplot(x=df['3Point%'], y=df['Points'], hue=df['Team'], palette='deep')
plt.title('Three-Point Percentage vs. Points Scored - 2022-2023 NBA Season')
plt.xlabel('Three-Point Percentage')
plt.ylabel('Points per Game')
plt.show()

# Defensive rating vs. number of wins (Team analysis)
plt.figure(figsize=(10,6))
sns.scatterplot(x=df['DefensiveRating'], y=df['Wins'], hue=df['Team'], palette='cool')
plt.title('Defensive Rating vs. Wins - 2022-2023 NBA Season')
plt.xlabel('Defensive Rating')
plt.ylabel('Wins')
plt.grid(True)
plt.show()

# Clutch games and top performers
clutch_games = df[df['Clutch'] == True]
clutch_performers = clutch_games.groupby('Player')['ClutchPoints'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=clutch_performers.index, y=clutch_performers, palette='rocket')
plt.title('Top 10 Clutch Performers - 2022-2023 NBA Season')
plt.xticks(rotation=45)
plt.ylabel('Clutch Points Scored')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

from analysis.player_data import create_players_dataset


def run():
    merged = create_players_dataset()

    # All the plots

    # Height and Win Rate
    # Calculate the average win rate by height
    win_rate_by_height = merged.groupby('HEIGHT')['WinRate'].mean()

    # Plot the data
    sns.scatterplot(x=win_rate_by_height.index, y=win_rate_by_height.values)
    # Link the points
    plt.plot(win_rate_by_height.index, win_rate_by_height.values, color='red')
    # Scope between 0 and 1 on the y-axis
    plt.ylim(0, 1)
    # Set the x-axis to start at 180 and end at 216
    plt.xlim(180, 216)
    # Add a title and axis labels
    plt.title('Win Rate by Height')
    plt.xlabel('Height (cm)')
    plt.ylabel('Win Rate')
    plt.show()

    # Height and Average Points per Game
    # Calculate the average points per game by height
    points_by_height = merged.groupby('HEIGHT')['AvgPointsPerGame'].mean()

    # Plot the data
    sns.scatterplot(x=points_by_height.index, y=points_by_height.values)
    # Link the points
    plt.plot(points_by_height.index, points_by_height.values, color='red')
    # Set the x-axis to start at 180 and end at 216
    plt.xlim(180, 216)
    # Add a title and axis labels
    plt.title('Average Points per Game by Height')
    plt.xlabel('Height (cm)')
    plt.ylabel('Average Points per Game')
    plt.show()

    # Position and average points per game and height multiplot plot
    # Create a DataFrame for each position (G, F, C, G-F, F-G, F-C, C-F)
    guards = merged[merged['POSITION'] == 'G']
    forwards = merged[merged['POSITION'] == 'F']
    centers = merged[merged['POSITION'] == 'C']
    guards_forwards = merged[merged['POSITION'] == 'G-F']
    forwards_guards = merged[merged['POSITION'] == 'F-G']
    forwards_centers = merged[merged['POSITION'] == 'F-C']
    centers_forwards = merged[merged['POSITION'] == 'C-F']

    # Calculate the average points per game by height for each position
    guards_points_by_height = guards.groupby('HEIGHT')['AvgPointsPerGame'].mean()
    forwards_points_by_height = forwards.groupby('HEIGHT')['AvgPointsPerGame'].mean()
    centers_points_by_height = centers.groupby('HEIGHT')['AvgPointsPerGame'].mean()
    guards_forwards_points_by_height = guards_forwards.groupby('HEIGHT')['AvgPointsPerGame'].mean()
    forwards_guards_points_by_height = forwards_guards.groupby('HEIGHT')['AvgPointsPerGame'].mean()
    forwards_centers_points_by_height = forwards_centers.groupby('HEIGHT')['AvgPointsPerGame'].mean()

    # Plot the data with subplots
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    # Add some space between the plots
    fig.subplots_adjust(hspace=0.5)
    axes[0, 0].scatter(x=guards_points_by_height.index, y=guards_points_by_height.values)
    axes[0, 0].plot(guards_points_by_height.index, guards_points_by_height.values, color='red')
    axes[0, 0].set_title('Guards')
    axes[0, 0].set_xlabel('Height (cm)')
    axes[0, 0].set_ylabel('Average Points per Game')
    axes[0, 0].set_ylim(0, 30)
    axes[0, 0].set_xlim(175, 230)
    axes[0, 1].scatter(x=forwards_points_by_height.index, y=forwards_points_by_height.values)
    axes[0, 1].plot(forwards_points_by_height.index, forwards_points_by_height.values, color='red')
    axes[0, 1].set_title('Forwards')
    axes[0, 1].set_xlabel('Height (cm)')
    axes[0, 1].set_ylabel('Average Points per Game')
    axes[0, 1].set_ylim(0, 30)
    axes[0, 1].set_xlim(175, 230)
    axes[1, 0].scatter(x=centers_points_by_height.index, y=centers_points_by_height.values)
    axes[1, 0].plot(centers_points_by_height.index, centers_points_by_height.values, color='red')
    axes[1, 0].set_title('Centers')
    axes[1, 0].set_xlabel('Height (cm)')
    axes[1, 0].set_ylabel('Average Points per Game')
    axes[1, 0].set_ylim(0, 30)
    axes[1, 0].set_xlim(175, 230)
    axes[1, 1].scatter(x=guards_forwards_points_by_height.index, y=guards_forwards_points_by_height.values)
    axes[1, 1].plot(guards_forwards_points_by_height.index, guards_forwards_points_by_height.values, color='red')
    axes[1, 1].set_title('Guards-Forwards')
    axes[1, 1].set_xlabel('Height (cm)')
    axes[1, 1].set_ylabel('Average Points per Game')
    axes[1, 1].set_ylim(0, 30)
    axes[1, 1].set_xlim(175, 230)
    axes[2, 0].scatter(x=forwards_guards_points_by_height.index, y=forwards_guards_points_by_height.values)
    axes[2, 0].plot(forwards_guards_points_by_height.index, forwards_guards_points_by_height.values, color='red')
    axes[2, 0].set_title('Forwards-Guards')
    axes[2, 0].set_xlabel('Height (cm)')
    axes[2, 0].set_ylabel('Average Points per Game')
    axes[2, 0].set_ylim(0, 30)
    axes[2, 0].set_xlim(175, 230)
    axes[2, 1].scatter(x=forwards_centers_points_by_height.index, y=forwards_centers_points_by_height.values)
    axes[2, 1].plot(forwards_centers_points_by_height.index, forwards_centers_points_by_height.values, color='red')
    axes[2, 1].set_title('Forwards-Centers')
    axes[2, 1].set_xlabel('Height (cm)')
    axes[2, 1].set_ylabel('Average Points per Game')
    axes[2, 1].set_ylim(0, 30)
    axes[2, 1].set_xlim(175, 230)
    plt.show()


if __name__ == '__main__':
    run()
player-height-scraper
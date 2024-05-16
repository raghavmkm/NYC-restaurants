import pandas as pd
import matplotlib.pyplot as plt

# Load the data
median_incomes = pd.read_csv('../data_deliverable/Clean/Median Incomes 2021 Clean.csv')
restaurant_data = pd.read_csv('../data_deliverable/Clean/Cleaned Restaurant data.csv')
violation_data = pd.read_csv('../data_deliverable/Clean/violations clean.csv')

def plot_dataset1():
    # Plot for Median Incomes
    plt.figure(figsize=(10, 8))  # Increase the figure size
    ax = median_incomes.plot(kind='bar', x='Neighbourhood', y='Median Household Income 2021', title='Median Household Income by Neighbourhood', color='skyblue')

    # Rotate to 90 degrees and adjust font size
    plt.xticks(rotation=90, fontsize=10)

    # Only show every nth label to avoid crowding (adjust n based on your specific data size)
    n = 5  # Adjust this number based on your total number of neighborhoods
    for index, label in enumerate(ax.xaxis.get_ticklabels()):
        if index % n != 0:
            label.set_visible(False)

    plt.ylabel('Income in USD')
    plt.xlabel('Neighbourhood')
    plt.tight_layout()
    plt.show()
    
def plot_dataset2():
    # # Plot for Restaurant Ratings
    # plt.figure(facecolor='white')
    # restaurant_data.dropna(subset=['Rating']).plot(kind='scatter', x='Rating', y='Rating Count', title='Restaurant Ratings vs. Rating Count', color='green')
    # plt.xlabel('Rating')
    # plt.ylabel('Rating Count')
    # plt.show()

    # Calculate the rating counts for each rating
    rating_counts = restaurant_data['Rating'].value_counts().sort_index()

    # Define colors for each bar
    colors = ['blue', 'green', 'red', 'purple', 'orange']

    # Plot histogram with different colors for each bar
    plt.figure(facecolor='white')
    plt.bar(rating_counts.index, rating_counts.values, color=colors, width=0.1)

    # Add title and labels
    plt.title('Restaurant Ratings Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Rating Count')

    # Show plot
    plt.show()

    

def plot_dataset3():
    # Plot for Violations
    plt.figure(facecolor='white')
    violation_data['VIOLATION CODE'].value_counts().head(10).plot(kind='bar', title='Top 10 Violation Codes', color='red')
    plt.xlabel('Violation Code')
    plt.ylabel('Frequency')
    plt.show()


def plot_model_1_metrics():
    # Metrics data
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1']
    values = [0.5406, 0.5560, 0.8472, 0.6707]
    errors = [0.0216, 0.0271, 0.0276, 0.0199]

    # Creating the bar chart with error bars
    colors = ['blue', 'green', 'red', 'purple']
    plt.figure(figsize=(10, 5), facecolor='white')
    plt.bar(metrics, values, yerr=errors, color=colors, capsize=5)
    plt.ylabel('Scores')
    plt.title('K-Fold Validation Results')
    plt.ylim(0, 1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_model_2_metrics():
    # Data
    cross_val_scores = [0.8, 0.8, 0.8, 0.76666667, 0.76666667, 0.76666667, 0.8, 0.8, 0.8, 0.8]
    mean_score = 0.79
    accuracy_test = 0.85

    # Plotting
    plt.figure(figsize=(12, 6), facecolor='white')
    plt.plot(cross_val_scores, label='Cross-Validation Scores', marker='o')
    plt.axhline(y=mean_score, color='r', linestyle='--', label='Mean Cross-Validation Score')
    plt.axhline(y=accuracy_test, color='g', linestyle='-.', label='Accuracy on Test Set')
    plt.xlabel('Fold Index')
    plt.ylabel('Score')
    plt.title('Cross-Validation Scores with Mean and Test Set Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    plot_dataset1()
    plot_dataset2()
    plot_dataset3()
    plot_model_1_metrics()
    plot_model_2_metrics()
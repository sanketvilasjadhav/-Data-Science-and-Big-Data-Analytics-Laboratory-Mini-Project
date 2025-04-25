# ... (Previous code remains unchanged up to df.head())

# 5. Histogram for First Dose Administered (distribution)
if 'First Dose Administered' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['First Dose Administered'].dropna(), kde=True, bins=30, color='skyblue')
    plt.title('Distribution of First Dose Administered')
    plt.xlabel('Number of Vaccinations')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# 6. Line Plot: First Dose Administered Over Time (for a specific state, e.g., Maharashtra)
if 'First Dose Administered' in df.columns and 'State' in df.columns and 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert Date column to datetime
    state_data = df[df['State'] == 'Maharashtra'].sort_values('Date')

    plt.figure(figsize=(12, 6))
    plt.plot(state_data['Date'], state_data['First Dose Administered'], marker='o', linestyle='-', color='green')
    plt.title('First Dose Administered Over Time in Maharashtra')
    plt.xlabel('Date')
    plt.ylabel('Number of Vaccinations')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 7. Heatmap for missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='Reds', yticklabels=False)
plt.title('Missing Data Heatmap')
plt.tight_layout()
plt.show()

# 8. Correlation Heatmap (only numeric columns)
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='YlGnBu')
plt.title('Correlation Between Features')
plt.tight_layout()
plt.show()

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Define the zip file path
zip_path = "/content/drive/MyDrive/dataset1/archive.zip"
extract_path = "/content/dataset_extracted"

# Extract the ZIP file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# List extracted files (to verify file name)
print("Extracted Files:")
print(os.listdir(extract_path))

# Set your actual CSV file name here (update if it's different)
csv_filename = "StatewiseTestingDetails.csv"  # Change if needed
csv_path = os.path.join(extract_path, csv_filename)

# Load CSV into DataFrame
df = pd.read_csv(csv_path)

# Display first few rows
df.head()

# 1. Describe Dataset
print("Dataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSummary Stats:")
print(df.describe())

# 2. State-wise first dose vaccinated (if applicable)
if 'First Dose Administered' in df.columns:
    df_state_first_dose = df.groupby('State')['First Dose Administered'].sum().sort_values(ascending=False)
    print("\nState-wise First Dose Administered:")
    print(df_state_first_dose)

    df_state_first_dose.plot(kind='bar', figsize=(12,6), title='First Dose Administered State-wise')
    plt.ylabel('Number of Vaccinations')
    plt.tight_layout()
    plt.show()

# 3. State-wise second dose vaccinated (if applicable)
if 'Second Dose Administered' in df.columns:
    df_state_second_dose = df.groupby('State')['Second Dose Administered'].sum().sort_values(ascending=False)
    print("\nState-wise Second Dose Administered:")
    print(df_state_second_dose)

    df_state_second_dose.plot(kind='bar', figsize=(12,6), color='orange', title='Second Dose Administered State-wise')
    plt.ylabel('Number of Vaccinations')
    plt.tight_layout()
    plt.show()

# 4. Number of Males and Females Vaccinated (if applicable)
if 'Male(Individuals Vaccinated)' in df.columns and 'Female(Individuals Vaccinated)' in df.columns:
    total_males = df['Male(Individuals Vaccinated)'].sum()
    total_females = df['Female(Individuals Vaccinated)'].sum()

    print(f"\nTotal Males Vaccinated: {total_males}")
    print(f"Total Females Vaccinated: {total_females}")

    plt.pie([total_males, total_females], labels=['Males', 'Females'], autopct='%1.1f%%', colors=['blue', 'pink'])
    plt.title('Male vs Female Vaccinated')
    plt.show()
else:
    print("Gender-wise vaccination data not available in this dataset.")

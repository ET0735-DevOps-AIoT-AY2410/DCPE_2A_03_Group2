import pandas as pd
import pytest

@pytest.fixture
def load_data():
    # Load the CSV file
    file_path = "gr_database.csv"
    return pd.read_csv(file_path)

def test_column_names(load_data):
    # Expected column names
    expected_columns = ["name","product_ID","price"]
    assert list(load_data.columns) == expected_columns, "Column names do not match"


def test_missing_values(load_data):
    # Ensure there are no missing values
    missing_values = load_data.isnull().sum().to_dict()
    assert all(value == 0 for value in missing_values.values()), "There are missing values in the data"

def test_sample_data(load_data):
    # Check for specific expected data rows
    expected_data = {"name": "carrot","product_ID":1234567890, "price": 2}
    assert expected_data in load_data.to_dict(orient="records"), "Expected row not found in data"

# Load the CSV file to analyze its structure
file_path = 'gr_database.csv'
df = pd.read_csv(file_path)

# Display basic information about the CSV file
df_info = {
    "columns": df.columns.tolist(),
    "missing_values": df.isnull().sum().to_dict(),
    "sample_data": df.head().to_dict(orient="records")
}

df_info

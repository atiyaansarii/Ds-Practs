import pandas as pd
from cryptography.fernet import Fernet

# Sample DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [28, 24, 30],
    'Salary': [50000, 60000, 55000],
    'Gender': ['Male', 'Female', 'Male']  
}
df = pd.DataFrame(data)

# Function to display data in horizontal style (wide format)
def horizontal_style(df):
    print("Horizontal Style Data (Wide Format):")
    print(df)

# Function to display data in vertical style (long format)
def vertical_style(df):
    df_vertical = pd.melt(df, id_vars=['Name'], var_name='Attribute', value_name='Value')
    print("\nVertical Style Data (Long Format):")
    print(df_vertical)

# Function to display data in island style (grouped by name)
def island_style(df):
    print("\nIsland Style Data:")
    grouped = df.groupby('Name')
    for name, group in grouped:
        print(f"\nIsland for {name}:")
        print(group)

# Function to display data in secure vault style (encrypting a column)
def secure_vault_style(df, column_to_encrypt):
    print("\nSecure Vault Style Data (With Encrypted Salary):")
    # Generate encryption key and cipher suite
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Encrypt the specified column
    df['Encrypted_' + column_to_encrypt] = df[column_to_encrypt].apply(
        lambda x: cipher_suite.encrypt(str(x).encode()).decode()
    )

    # Drop the original column after encryption
    df_secure_vault = df.drop(columns=[column_to_encrypt])
    print(df_secure_vault)

    # Decrypt for verification
    df_secure_vault['Decrypted_' + column_to_encrypt] = df_secure_vault[
        'Encrypted_' + column_to_encrypt].apply(
        lambda x: cipher_suite.decrypt(x.encode()).decode()
    )

    print("\nDecrypted Salary for Verification:")
    print(df_secure_vault[['Name', 'Decrypted_' + column_to_encrypt]])

# Calling the functions
horizontal_style(df)
vertical_style(df)
island_style(df)
secure_vault_style(df, 'Salary')

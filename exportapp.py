from google.colab import files

customers_df.to_csv('customers_df.csv') 
files.download('customers_df.csv')
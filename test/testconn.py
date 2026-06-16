import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv
load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET_ID = os.getenv("GCP_DATASET_ID")
TABLE_ID = "test_sales"
full_table_path = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# ข้อมูลทดสอบ
data = {
    'order_id': [1001, 1002],
    'product_name': ['Laptop', 'Mouse'],
    'total_revenue': [45000.00, 1200.00]
}
df = pd.DataFrame(data)

print("🔒 Connecting to BigQuery using Secure Application Default Credentials...")
client = bigquery.Client(project=PROJECT_ID)

try:
    # สั่งส่งข้อมูลขึ้น Cloud
    job = client.load_table_from_dataframe(df, full_table_path)
    job.result()  # รอ
    print(f" SUCCESS! Loaded data to {full_table_path}")


except Exception as e:
    print(f"❌ เกิดข้อผิดพลาด: {e}")
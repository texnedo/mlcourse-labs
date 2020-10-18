import psycopg2
import pandas as pd

def main():
    'https://www.kaggle.com/raosuny/e-commerce-purchase-dataset'
    purchase_df = pd.read_csv("/Users/texnedo/Downloads/purchase_data_exe.csv")
    print(purchase_df.head().to_json())
    print(purchase_df.head())
    print(purchase_df['customer_id'])
    purchase_df['date'] = pd.to_datetime(purchase_df['date'], format="%d/%m/%Y")
    conn = psycopg2.connect(
        database="purchase", user='postgres', password='mysecretpassword', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    for index, row in purchase_df.iterrows():
        statement = '''INSERT INTO purchases(purchase_date, customer_id, product_category, payment_method,
                            value_USD, time_on_site_MINS, clicks_in_site)
                            VALUES ('{}',{},{},'{}',{},{},{})'''
        statement = statement.format(
            row['date'].strftime("%Y-%m-%d"),
            row['customer_id'],
            row['product_category'],
            row['payment_method'],
            row['value [USD]'],
            row['time_on_site [Minutes]'],
            row['clicks_in_site']
        )
        cursor.execute(statement)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()

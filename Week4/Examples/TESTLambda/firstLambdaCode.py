import json
import boto3
from io import StringIO

def lambda_handler(event, context):

    s3 = boto3.client('s3')
    
    bucket="retail-etlfeb17"

    #key will return path including file name after the bucket name above
    key = event['Records'][0]['s3']['object']['key']

    obj=s3.get_object(Bucket=bucket,Key=key)
    data = json.loads(obj['Body'].read())

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "price",
        "total_amount"
    ])

    for order in data:
        for item in order["items"]:
            total=item["quantity"]*item["price"]
            writer.writerow([
                order["order_id"],
                order["customer_id"],
                item["product_id"],
                order["order_date"],
                item["quantity"],
                item["price"],
                total
            ])
    s3.put_object(
        Bucket=bucket,
        Key="processed/orders_flat.csv",
        Body=output.getvalue()
    )

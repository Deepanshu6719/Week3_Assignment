# function based solution so products.csv and output.csv files name 
import csv

TAX_RATE = 18


def calculate_price(cost_price):
    sales_tax = cost_price * TAX_RATE / 100
    final_price = cost_price + sales_tax

    return sales_tax, final_price


def read_products(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        products = []

        for row in reader:
            products.append(row)

    return products


def generate_output(products, filename):
    with open(filename, "w", newline="") as file:

        fieldnames = [
            "Product-Name",
            "Product-CostPrice",
            "Product-SalesTax",
            "Product-FinalPrice",
            "Country"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for product in products:

            cost_price = float(product["Product-CostPrice"])

            sales_tax, final_price = calculate_price(cost_price)

            writer.writerow({
                "Product-Name": product["Product-Name"],
                "Product-CostPrice": f"{cost_price:.2f}",
                "Product-SalesTax": f"{sales_tax:.2f}",
                "Product-FinalPrice": f"{final_price:.2f}",
                "Country": product["Country"]
            })


products = read_products("products.csv")

generate_output(products, "output.csv")

print("Output file generated successfully.")
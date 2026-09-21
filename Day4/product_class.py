# class based solution so product1.csv and output1.csv filename

import csv


class Product:

    TAX_RATE = 18

    def __init__(self, name, cost_price, country):
        self.name = name
        self.cost_price = cost_price
        self.country = country

    def calculate_tax(self):
        return self.cost_price * self.TAX_RATE / 100

    def calculate_final_price(self):
        return self.cost_price + self.calculate_tax()


def read_products(filename):

    products = []

    with open(filename, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            product = Product(
                row["Product-Name"],
                float(row["Product-CostPrice"]),
                row["Country"]
            )

            products.append(product)

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

            writer.writerow({
                "Product-Name": product.name,
                "Product-CostPrice": f"{product.cost_price:.2f}",
                "Product-SalesTax": f"{product.calculate_tax():.2f}",
                "Product-FinalPrice": f"{product.calculate_final_price():.2f}",
                "Country": product.country
            })


products = read_products("product1.csv")

generate_output(products, "output1.csv")

print("Output file generated successfully.")
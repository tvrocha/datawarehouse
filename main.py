import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Set random seed for reproducibility
random.seed(42)

# Generate random purchase data
data = []
for _ in range(100):
    email_vendedor = fake.email()
    data_compra = fake.date_this_year()
    hora_compra = fake.time(pattern='%H:%M')
    valor_compra = round(random.uniform(100, 15000), 2)
    unidades_vendidas = random.randint(1, 100)
    loja_origem = random.choice(['Loja Física', 'Loja Online', 'Terceiros'])
    
    data.append([email_vendedor, data_compra, hora_compra, valor_compra, unidades_vendidas, loja_origem])

# Create DataFrame
df = pd.DataFrame(data, columns=['Email do Vendedor', 'Data da Compra', 'Hora da Compra', 'Valor da Compra', 'Unidades Vendidas', 'Origem do Produto'])

# Show the table
print(df.head())

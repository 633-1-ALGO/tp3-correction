from domaine.customer import Customer
from metier.customers import CustomerTree
from outils.file_loader import FileLoader
from outils.file_parser import FileParser
from outils.file_writer import FileWriter

loader = FileLoader()
parser = FileParser()
writer = FileWriter()
file_content = loader.load("data/costumers_data.csv")
costumers = parser.parse_costumers(file_content)

file_content = loader.load("data/costumers_relations.csv")
relations = parser.parse_relations(file_content)

customer_tree = CustomerTree()
customer_tree.build_tree(costumers, relations)

# Tests ...

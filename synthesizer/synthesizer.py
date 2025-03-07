import xml.etree.ElementTree as ET

from faker import Faker

fake = Faker()


def generate_json_data(data):
    """
    Generate JSON data based on specified data types.

    Parameters:
    - data_types: A dictionary where keys are JSON keys and values are data types.
                  Supported data types are 'name', 'email', 'phone_number', 'address',
                  'text', 'integer', 'float', 'boolean', 'date', 'datetime'.

    Returns:
    - A dictionary representing the generated data.
    """
    # Generate data based on data_types here...
    # For demonstration, assume data is already generated
    return data


# Usage
data_types = {
    "name": "name",
    "email": "email",
    "phone": "phone_number",
    "address": "address",
    "description": "text",
    "age": "integer",
    "height": "float",
    "is_active": "boolean",
    "created_at": "date",
    "updated_at": "datetime"
}

myjson_object = generate_json_data(data_types)
name = myjson_object["name"]


# Example usage
# data_types = {
#     'name': 'name',
#     'email': 'email',
#     'phone': 'phone_number',
#     'address': 'address',
#     'description': 'text',
#     'age': 'integer',
#     'height': 'float',
#     'is_active': 'boolean',
#     'created_at': 'date',
#     'updated_at': 'datetime'
# }

def generate_xml_data(data_types):
    """
    Generate XML data based on specified data types.

    Parameters:
    - data_types: A dictionary where keys are XML tags and values are data types.
                  Supported data types are 'name', 'email', 'phone_number', 'address',
                  'text', 'integer', 'float', 'boolean', 'date', 'datetime'.

    Returns:
    - An XML string representing the generated data.
    """
    root = ET.Element("data")

    for tag, dtype in data_types.items():
        element = ET.SubElement(root, tag)

        if dtype == 'name':
            element.text = fake.name()
        elif dtype == 'email':
            element.text = fake.email()
        elif dtype == 'phone_number':
            element.text = fake.phone_number()
        elif dtype == 'address':
            element.text = fake.address()
        elif dtype == 'text':
            element.text = fake.text()
        elif dtype == 'integer':
            element.text = str(fake.random_int(min=0, max=1000))
        elif dtype == 'float':
            element.text = str(fake.random_int(min=0, max=1000) + fake.random_int(min=0, max=99) / 100)
        elif dtype == 'boolean':
            element.text = str(fake.random_element(elements=(True, False)))
        elif dtype == 'date':
            element.text = str(fake.date())
        elif dtype == 'datetime':
            element.text = fake.date_time().isoformat()
        else:
            raise ValueError(f"Unsupported data type: {dtype}")

    # Convert the ElementTree to a string
    xml_string = ET.tostring(root, encoding='unicode')

    return xml_string


# Example usage
data_types = {
    'name': 'name',
    'email': 'email',
    'phone': 'phone_number',
    'address': 'address',
    'description': 'text',
    'age': 'integer',
    'height': 'float',
    'is_active': 'boolean',
    'created_at': 'date',
    'updated_at': 'datetime'
}

print(generate_xml_data(data_types))

from faker import Faker

fake = Faker()


def synthesize_json_data(data_types):
    """
    Generate a dictionary with synthesized data based on the specified data types.

    :param data_types: A dictionary where keys are field names and values are data types.
    :return: A dictionary with generated fake data.
    """
    generated_data = {}

    for key, data_type in data_types.items():
        if data_type == "name":
            generated_data[key] = fake.name()
        elif data_type == "email":
            generated_data[key] = fake.email()
        elif data_type == "phone_number":
            generated_data[key] = fake.phone_number()
        elif data_type == "address":
            generated_data[key] = fake.address()
        elif data_type == "text":
            generated_data[key] = fake.text()
        elif data_type == "integer":
            generated_data[key] = fake.random_int(min=0, max=100)
        elif data_type == "float":
            generated_data[key] = round(fake.random.uniform(0, 100), 2)
        elif data_type == "boolean":
            generated_data[key] = fake.boolean()
        elif data_type == "date":
            generated_data[key] = fake.date().format()
        elif data_type == "datetime":
            generated_data[key] = fake.date_time().isoformat()
        else:
            generated_data[key] = f"Unsupported data type: {data_type}"

    return generated_data


# Example usage
if __name__ == "__main__":
    data_types = {
        "full_name": "name",
        "user_email": "email",
        "contact_number": "phone_number",
        "home_address": "address",
        "random_text": "text",
        "age": "integer",
        "salary": "float",
        "is_active": "boolean",
        "dob": "date",
        "last_login": "datetime",
        "unsupported_field": "unknown_type"
    }

    generated_sample = synthesize_json_data(data_types)
    print(generated_sample)

# Usage
data_types = {
    "name": "name",
    "email": "email",
    "phone": "phone_number",
    "address": "address",
    "description": "text",
    "age": "integer",
    "height": "float",
    "is_active": "boolean",
    "created_at": "date",
    "updated_at": "datetime"
}

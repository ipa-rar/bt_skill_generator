#!/usr/bin/python
import jinja2

class SkillCodeGenerator:

    def __init__(self):
        self.class_name = None
        self.ports = []
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        templateEnv = jinja2.Environment(loader=templateLoader)
        self.stateful_bt_skill_template = templateEnv.get_template('stateful_bt_skill_template.j2')
        self.sync_bt_skill_template = templateEnv.get_template('sync_bt_skill_template.j2')

    def get_port_input(self, port_type):
        name = input("Enter the name of the port: ")
        data_type = input(f"Enter the data type of {name} port: ")
        default_value = input(f"Enter the default value of {name} port (Press Enter to skip): ")
        description = input(f"Enter the description of {name} port: ")
        return {"name": name, "data_type": data_type, "default_value": default_value, "description": description}

    def get_user_inputs(self):
        self.class_name = input("Enter the class name: ")

        num_ports = int(input("Enter the number of ports: "))
        for i in range(num_ports):
            port_type = input(f"Enter the port type (Input/Output): ").capitalize()
            self.ports.append({"port_type": port_type, **self.get_port_input(port_type)})

    def generate_code(self):
        self.get_user_inputs()

        # Create a Jinja template and render it with user inputs
        template = self.stateful_bt_skill_template
        generated_code = template.render(CLASS_NAME=self.class_name, ports=self.ports)

        # Save the generated code to a file
        output_file = f"generated/{self.class_name.lower()}_node.hpp"
        with open(output_file, "w") as file:
            file.write(generated_code)

        print(f"Code generation complete! The C++ header file '{output_file}' has been created.")

if __name__ == "__main__":
    generator = SkillCodeGenerator()
    generator.generate_code()

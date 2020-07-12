from dataclasses import dataclass


@dataclass
class MyContainer:
    attribute_a: str
    attribute_b: str


if __name__ == "__main__":
    container_inst1 = MyContainer(attribute_a="value_a", attribute_b="value_b")
    container_inst2 = MyContainer(attribute_a="value_c", attribute_b="value_d")
    container_inst3 = MyContainer(attribute_a="value_a", attribute_b="value_b")

    print(f"Attribute A: {container_inst1.attribute_a}, Attribute B: {container_inst1.attribute_b}")
    print(f"Container Inst1 equal Inst2?: {container_inst1==container_inst2}")
    print(f"Container Inst1 equal Inst3?: {container_inst1 == container_inst3}")

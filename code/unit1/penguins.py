import csv


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def read_penguin_data():
    with open("datasets/penguins_size.csv") as f:
        penguin_data = {}
        count_dream = 0
        for row in csv.DictReader(f):
            ## This is a one-off, a little annoying
            if row["island"] == "Dream" and row["species"] == "Chinstrap":
                count_dream += 1
            if row["species"] not in penguin_data:
                penguin_data[row["species"]] = {}
                penguin_data[row["species"]]["count"] = 1

                if is_float(row["culmen_length_mm"]):
                    penguin_data[row["species"]]["sum_culmen_length"] = float(
                        row["culmen_length_mm"]
                    )
                    penguin_data[row["species"]]["sum_mass"] = float(row["body_mass_g"])
                    penguin_data[row["species"]]["count_float"] = 1

            else:
                if is_float(row["culmen_length_mm"]):
                    penguin_data[row["species"]]["sum_culmen_length"] += float(
                        row["culmen_length_mm"]
                    )
                    penguin_data[row["species"]]["sum_mass"] += float(
                        row["body_mass_g"]
                    )
                    penguin_data[row["species"]]["count_float"] += 1
                penguin_data[row["species"]]["count"] += 1
    print(f"Number of Chinstrap penguins from Dream Island: {count_dream}")
    print(penguin_data)
    return penguin_data


def get_max(penguin_data, key):
    averages = [
        (species, penguin_data[species][key] / penguin_data[species]["count_float"])
        for species in penguin_data
    ]
    return max(averages, key=lambda x: x[1])

penguin_data = read_penguin_data()

print(
    f"Species with greatest average bill size: {get_max(penguin_data, "sum_culmen_length")}"
)
print(f"Species with greatest average mass: {get_max(penguin_data, "sum_mass")}")

from ninja import NinjaAPI
import csv

api = NinjaAPI()


@api.get("/filter-frequent-items")
def filter_frequent_items(request):
    return {"test": "success"}


@api.get("/get-all-frequent-items")
def get_all_association_rules(request):
    assoc_rules = []
    with open("market/data/converted_assoc_rules.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the first row
        for row in reader:
            assoc_rule = {}
            assoc_rule.update(
                {
                    "Selected products: ": eval(row[1]),
                    "Recommended: ": eval(row[2]),
                    "Confidence: ": row[3],
                }
            )
            assoc_rules.append(assoc_rule)
    return assoc_rules


@api.get("/get-all-frequent-items-by-category")
def get_all_association_rules_by_category(request):
    assoc_rules = []
    with open(
        "market/data/converted_association_rules_category.csv", newline=""
    ) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the first row
        for row in reader:
            assoc_rule = {}
            assoc_rule.update(
                {
                    "Selected products: ": eval(row[1]),
                    "Recommended: ": eval(row[2]),
                    "Confidence: ": row[3],
                }
            )
            assoc_rules.append(assoc_rule)
    return assoc_rules

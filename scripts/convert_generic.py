import json
import sys


def convert_data(table: str, data: list) -> str:
    queries = []

    for item in data:
        # dynamically infer all keys from item and add them to query
        keys = ", ".join(item.keys())
        values = ", ".join([f"'{value}'" for value in item.values()])
        query = f"""INSERT INTO {table} ({keys})
        VALUES ({values});
        """

        queries.append(query)

    return "\n".join(queries)


if __name__ == "__main__":
    table_name = sys.argv[1]
    file = sys.argv[2]

    with open(f"./scripts/{file}.json", encoding="utf-8") as f:
        data = json.load(f)

    with open(f"./scripts/{file}.sql", "w", encoding="utf-8") as f:
        f.write(convert_data(table_name, data))

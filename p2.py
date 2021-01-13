import csv

with open("p2.csv", "r") as csvFile:
    D = list(csv.reader(csvFile))
num_attrs = len(D[0]) - 1

S = ["0"] * num_attrs
G_null = [["?"] * num_attrs]
print(f"S0: {S}")
print(f"G0: {G_null}")

S = D[0][:num_attrs]
G = []

for i in range(0, len(D)):
    train_data = D[i]

    if train_data[-1] == "Yes":
        for j in range(num_attrs - 1):
            if train_data[j] != S[j]:
                S[j] = "?"

        for j in range(num_attrs - 1):
            for k in range(1, len(G)):
                if G[k][j] != S[j] != "?":
                    del G[k]

    elif train_data[-1] == "No":
        for j in range(num_attrs - 1):
            if train_data[j] != S[j] != "?":
                g = ["?"] * num_attrs
                g[j] = S[j]
                G.append(g)

    print("-" * 10)
    print(f"D{i + 1}: {train_data}")
    print(f"S{i + 1}: {S}")
    print(f"G{i + 1}: {G_null if not G else G}")
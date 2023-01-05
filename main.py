from csv import reader
import sys

table = sys.argv[1]

def file(table=str(table)):
    with open(table) as file:
        data = reader(file)
        return [row for row in data]

def convert():
    values = file()
    print("\\begin{table}[!ht]")
    print("\\centering")
    print("\\caption{Table}")
    print("\\begin{tabular}{%s}" % ("c" * len(values[0])))
    print("\\toprule")
    for i in values:
        for j in range(len(i)):
            # if i == values[0]:
            #     print("\\textbf{%s}" % i[j], end="")
            if j == 0 and values.index(i) == 1:
                print("\\midrule")
            if j == len(i) - 1 and values.index(i) != 0:
                print(i[j], end=' \\\\\n')
            elif i == values[0]:
                if j == len(i) - 1:
                    print("\\textbf{%s}" % i[j], end=' \\\\\n')
                else:
                    print("\\textbf{%s}" % i[j], end=" & ")
            else:
                print(i[j], end=' & ')

    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\end{table}")

if __name__ == "__main__":
    convert()

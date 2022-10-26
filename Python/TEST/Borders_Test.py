with open("TEST/Borders_Test.txt", 'a') as f:
    f.truncate(0)
    rows = 100
    columns = rows
    f.write(f"{rows} {columns}\n")
    choicesArray = ['0', '1']
    for row in range(rows):
        choice = row % 2
        gridString = ""
        for column in range(columns):
            choice = choice ^ 1
            gridString += choicesArray[choice]
        f.write(f"{gridString}\n")

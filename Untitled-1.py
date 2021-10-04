def mapping_c(df, operators, l, c):
    # print(df.loc[l, c])
    value = df.loc[l, c].split(' ')
    str = ""

    print(value)

    for cell in value:
        
        # print('cell', cell)
        # break

        while True:
            if cell not in operators and not cell.isdigit():
                l = cell[:1]
                c = int(cell[1:])
                # if not cell.isdigit():
                value = df.loc[l, c]
                print(value)
                if not any(cc in string.ascii_uppercase for cc in value):
                    print(str)
                    str = str + value
                else:
                    return str + mapping_c(df, operators, l, c)
                # l = value[:1]
                # c = int(value[1:])
            else:
                str = cell + ' ' + str

    # return value

print(mapping_c(df, operators, 'B', 0))



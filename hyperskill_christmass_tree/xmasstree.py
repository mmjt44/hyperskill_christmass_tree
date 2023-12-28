def create_postcard(width=50,height=30):
    postcard = []
    for i in range(height):
        line = []
        for j in range(width):
            if i ==0 or i==height -1 :
                line.append("-")
            elif j == 0 or j == width - 1:
                line.append("|")
            else:
                line.append(" ")
        postcard.append(line)

    return postcard

def add_text_to_postcard(postcard):
    text = "Merry Xmas"
    text_list = list(text)

    line_to_replace = postcard[len(postcard)-3]
    del line_to_replace[20:25]
    line_to_replace[20:25]  = text_list

    postcard[len(postcard)-3] = line_to_replace

    return postcard


def create_christmas_tree(height, interval):
    widht = height * 2 - 1
    array = []
    space = height - 1
    deco = 0

    for i in range(height):
        line = []
        k = 1
        for j in range(widht):
            if j < space or j > widht - space - 1:
                line.append(" ")
            else:
                if j == space:
                    line.append("/")
                elif j == widht - space - 1:
                    line.append("\\")
                else:
                    if k % 2 == 0:
                        deco = deco + 1
                        if deco % interval == 1 or interval == 1:
                            line.append('O')
                        else:
                            line.append('*')
                    else:
                        line.append("*")
                    k = k + 1
        space = space - 1
        array.append(line)

    # add X
    x_line = array[0]
    x_line = ['X' if x == '/' else x for x in x_line]
    array.insert(0,x_line)

    # add tree bottom
    bottom_line = []
    for j in range(widht):
        if j == height - 2 or j == height:
            bottom_line.append("|")
        else:
            bottom_line.append(" ")

    array.append(bottom_line)

    # replace first *
    second_line = ['^' if x == '/' else x for x in array[1]]
    array.remove(array[1])
    array.insert(1, second_line)

    return array


def add_christmas_tree_to_postcard(postcard, tree, x, y):
    tree_width = len(tree[0])
    tree_height = len(tree)
    x = int(x)
    y = int(y)
    height = 0
    for row in postcard:
        width = 0
        if height >= y and height <= (y + tree_height -1):
            int_tree_width = 0
            for j in row:
                if width >= (x - tree_width // 2) and width <= (x + tree_width // 2):
                    if row[width] == " ":
                        row[width] = tree[height-y][int_tree_width]
                    int_tree_width = int_tree_width + 1
                width = width + 1
            postcard[height] = row
        height = height + 1

    return postcard

def print_postcard(postcard):
    for row in postcard:
        print("".join(str(x) for x in row))

def main():
    try:
        input_parameters = input().split(" ")

        if len(input_parameters) == 2:
            height = int(input_parameters[0])
            if height < 3:
                raise Exception('Height of Christmass Tree must be greater than 3')
            interval = int(input_parameters[1])
            postcard = create_christmas_tree(height, interval)
        elif len(input_parameters) > 2 and len(input_parameters) % 4 != 0:
            raise Exception('For each Christmas tree please provide 4 parameters: Height, Interval, Line and Column')
        else:
            postcard = create_postcard()
            postcard = add_text_to_postcard(postcard)

            while len(input_parameters) % 4 == 0 and len(input_parameters) != 0:
                christmas_tree_parameters = input_parameters[-4:]
                height = int(christmas_tree_parameters[0])
                if height < 3:
                    raise Exception('Height of Christmass Tree must be greater than 3')
                interval = int(christmas_tree_parameters[1])
                line = int(christmas_tree_parameters[2])
                column = int(christmas_tree_parameters[3
                             ])
                christmass_tree = create_christmas_tree(height, interval)
                postcard = add_christmas_tree_to_postcard(postcard, christmass_tree, column, line)
                input_parameters = input_parameters[0:-4]


        print_postcard(postcard)


    except ValueError:
        print("Please provide intiger")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
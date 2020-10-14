colors_file = open("colors.txt", "r")
training_colors = open("palettes_dataRGBline_FORMATED.txt", "r")

lines = colors_file.readlines()
t_colors = training_colors.readlines()


colors_dict = {}
for line in lines:
    name = line[:line.find(' ')]
    values = line[line.find(' '):line.find('\n')]
    values = values.split(" ")
    values = [int(values[1]), int(values[2]), int(values[3])]
    colors_dict[name] = values

final_str = ""
all_palettes_list = []
current_palette_colors = []
i = 1
for color in t_colors:
    cor = color[:line.find(' \n')]
    cor = cor.split(" ")
    cor = [int(cor[0]), int(cor[1]), int(cor[2])]

    found = False
    for k, v in colors_dict.items():
        if found:
            break
        redRange = range(v[0] - 10, v[0] + 10)
        greenRange = range(v[1] - 10, v[1] + 10)
        blueRange = range(v[2] - 10, v[2] + 10)
        if cor[0] in redRange and cor[1] in greenRange and cor[2] in blueRange:
            current_palette_colors.append({k: cor})
            # final_str += str(cor[0]) + " " + str(cor[1]) + " " + str(cor[2]) + " " + k + '\n'
            found = True

    if not found:
        for k, v in colors_dict.items():
            if found:
                break
            redRange = range(v[0] - 20, v[0] + 20)
            greenRange = range(v[1] - 20, v[1] + 20)
            blueRange = range(v[2] - 20, v[2] + 20)
            if cor[0] in redRange and cor[1] in greenRange and cor[2] in blueRange:
                current_palette_colors.append({k: cor})
                # final_str += str(cor[0]) + " " + str(cor[1]) + " " + str(cor[2]) + " " + k + '\n'
                found = True

    if not found:
        for k, v in colors_dict.items():
            if found:
                break
            redRange = range(v[0] - 25, v[0] + 25)
            greenRange = range(v[1] - 25, v[1] + 25)
            blueRange = range(v[2] - 25, v[2] + 25)
            if cor[0] in redRange and cor[1] in greenRange and cor[2] in blueRange:
                current_palette_colors.append({k: cor})
                # final_str += str(cor[0]) + " " + str(cor[1]) + " " + str(cor[2]) + " " + k + '\n'
                found = True

    if not found:
        for k, v in colors_dict.items():
            if found:
                break
            redRange = range(v[0] - 30, v[0] + 30)
            greenRange = range(v[1] - 30, v[1] + 30)
            blueRange = range(v[2] - 30, v[2] + 30)
            if cor[0] in redRange and cor[1] in greenRange and cor[2] in blueRange:
                current_palette_colors.append({k: cor})
                # final_str += str(cor[0]) + " " + str(cor[1]) + " " + str(cor[2]) + " " + k + '\n'
                found = True

    if not found:
        for k, v in colors_dict.items():
            if found:
                break
            redRange = range(v[0] - 35, v[0] + 35)
            greenRange = range(v[1] - 35, v[1] + 35)
            blueRange = range(v[2] - 35, v[2] + 35)
            if cor[0] in redRange and cor[1] in greenRange and cor[2] in blueRange:
                current_palette_colors.append({k: cor})
                # final_str += str(cor[0]) + " " + str(cor[1]) + " " + str(cor[2]) + " " + k + '\n'
                found = True

    if not found:
        for k, v in colors_dict.items():
            if found:
                break
            redRange = range(v[0] - 39, v[0] + 39)
            greenRange = range(v[1] - 39, v[1] + 39)
            blueRange = range(v[2] - 39, v[2] + 39)
            if cor[0] in redRange and cor[1] in greenRange and cor[2] in blueRange:
                current_palette_colors.append({k: cor})
                # final_str += str(cor[0]) + " " + str(cor[1]) + " " + str(cor[2]) + " " + k + '\n'
                found = True

    if not found:
        for k, v in colors_dict.items():
            if found:
                break
            redRange = range(v[0] - 40, v[0] + 40)
            greenRange = range(v[1] - 40, v[1] + 40)
            blueRange = range(v[2] - 40, v[2] + 40)
            if cor[0] in redRange and cor[1] in greenRange and cor[2] in blueRange:
                current_palette_colors.append({k: cor})
                # final_str += str(cor[0]) + " " + str(cor[1]) + " " + str(cor[2]) + " " + k + '\n'
                found = True

    if i % 5 == 0:
        all_palettes_list.append(list(current_palette_colors))
        current_palette_colors.clear()

    i +=1
def print_towers():
    result = ""
    for tower in game:
        result += str(tower) + "\n"
    print("\n"+result)
    
def move_disk(layer_number, from_tower, to_tower, axiliary_tower):
    if layer_number == 1:
        to_tower.append(from_tower.pop())
        print_towers()
        return
    move_disk(layer_number - 1, from_tower, axiliary_tower, to_tower)
    move_disk(1, from_tower, to_tower, axiliary_tower)
    move_disk(layer_number - 1, axiliary_tower, to_tower, from_tower)
    return

game = [[], [], []]
if __name__ == "__main__":
    num_layers = int(input("Enter number of layers: "))
    game[0] = list(range(num_layers, 0, -1))
    print_towers()
    move_disk(num_layers, game[0], game[2], game[1])
    print_towers()

def location(block):
    #we need to start from after the co-ordinates
    location_start = block.find(" ")
    location_end = len(block)-1
    location = block[location_start:location_end + 1]
    #reversing the reverse name
    return  location[::-1].title()


def temperature(block):
    #pretty self explainatory
    temp_start = 0
    temp_end = block.find("_")
    temp = block[temp_start:temp_end]
    #conv to float
    return float(temp)

def x_coordinate(block):
    x_start = block.find(":") + 1
    x_end = block.find(",")
    x = block[x_start:x_end]
    return x

def y_coordinate(block):
    y_start = block.find(",") + 1
    y_end = block.find(" ")
    y = block[y_start:y_end]
    return y

def pressure(block):
    p_start = block.find("_") + 1
    p_end = block.find(":")
    p = block[p_start:p_end]
    #needa conv to float
    return float(p)

def get_block(data):
    block_start = data.find("BEGIN") + 6 #+6 because we need to go from the start of begin to the first letter of the block
    block_end = data.find("END")
    return data[block_start:block_end]

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()

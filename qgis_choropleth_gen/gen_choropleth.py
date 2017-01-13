bottom = 0
top = 100
num_classes = 50
colours = [[215, 25, 28], [254, 238, 171], [43, 131, 186]]

increment = (top - bottom) / num_classes
col_levels = num_classes / (len(colours) - 1) 

col_increments = []

for i in (0..len(colours) - 1):
    
    inc = []
    inc.append((colours[i + 1][0] - colours[i][0]) / col_levels)
    inc.append((colours[i + 1][1] - colours[i][1]) / col_levels)
    inc.append((colours[i + 1][2] - colours[i][2]) / col_levels)
    col_increments.append(inc)
    
i_col = 0

for i in (0..(num_classes - 1)):
    
    r = hex(colours[i_col][0] + col_increments[i_col][0]).split('x')[1]    
    g = hex(colours[i_col][1] + col_increments[i_col][1]).split('x')[1]
    b = hex(colours[i_col][2] + col_increments[i_col][2]).split('x')[1]
    
    val_bot = bottom + i * increment 
    val_top = val_bot + increment
    
    i_col = i_col + num_classes / col_levels
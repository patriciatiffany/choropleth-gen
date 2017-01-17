outputFilePath = "out.sld"

bottom = 21.1
top = 37.5
num_classes = 50
colours = [[215, 25, 28], [254, 238, 171], [43, 131, 186]]


increment = (top - bottom) / num_classes
col_levels = num_classes / (len(colours) - 1) 

col_increments = []

rules = ""

header = """<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" units="mm" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>test8DEMFinal.hasc output Polygon</se:Name>
    <UserStyle>
      <se:Name>test8DEMFinal.hasc output Polygon</se:Name>
      <se:FeatureTypeStyle>
"""

footer = """
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
"""


def create_level(bot, top, colour):
    
    return """        <se:Rule>
          <se:Name> """ + str(bot) + " - " + str(top) + """ </se:Name>
          <se:Description>
            <se:Title> """ + str(bot) + " - " + str(top) + """ </se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:PropertyName>value</ogc:PropertyName>
                <ogc:Literal>""" + str(bot) + """</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:PropertyName>value</ogc:PropertyName>
                <ogc:Literal>""" + str(top) + """</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#""" + colour + """</se:SvgParameter>
            </se:Fill>
            <se:Stroke>
              <se:SvgParameter name="stroke">#""" + colour + """</se:SvgParameter>
              <se:SvgParameter name="stroke-width">0</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
            </se:Stroke>
          </se:PolygonSymbolizer>
        </se:Rule> """


for i in range(len(colours) - 1):
    
    inc = []
    inc.append((colours[i + 1][0] - colours[i][0]) / col_levels)
    inc.append((colours[i + 1][1] - colours[i][1]) / col_levels)
    inc.append((colours[i + 1][2] - colours[i][2]) / col_levels)
    col_increments.append(inc)
    
# Colour increments for last class    
col_increments.append([0,0,0])    
i_col = 0

for i in range(num_classes):
    
    num_inc = i % col_levels
    
    try:
        r = hex(int(colours[i_col][0] + num_inc * col_increments[i_col][0])).split('x')[1]    
        g = hex(int(colours[i_col][1] + num_inc * col_increments[i_col][1])).split('x')[1]
        b = hex(int(colours[i_col][2] + num_inc * col_increments[i_col][2])).split('x')[1]
    except Exception:
        print ("Exception: " + str(i_col) + " " + str(num_inc))
    
    val_bot = bottom + i * increment 
    val_top = val_bot + increment
    
    i_col = int((i + 1) / col_levels)
    
    rules = rules + create_level(val_bot, val_top, r + g + b)
    

text_file = open(outputFilePath, "w")
text_file.write(header)
text_file.write(rules)
text_file.write(footer)
text_file.close()

        
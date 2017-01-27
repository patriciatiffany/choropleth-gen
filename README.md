Choropleth generator for QGIS
===============================================================================


Copyright
-------------------------------------------------------------------------------

Copyright (c) 2017 Luís Moreira de Sousa. All rights reserved. 
Any use of this software constitutes full acceptance of all terms of the 
document licence.


Description
-------------------------------------------------------------------------------

Generates choropleths for vector files, taking into account the idiosyncrasies 
of QGIS. They are useful, for instance, to style [HexASCII](https://github.com/ldesousa/HexAsciiBNF) rasters.



Install
-------------------------------------------------------------------------------

This package can be installed from [PyPi](https://pypi.python.org/pypi?%3Aaction=pkg_edit&name=choropleth-gen), issuing a command like:

`pip install choropleth-gen`

Usage
-------------------------------------------------------------------------------

The package installs two scripts in the system: `gen_greyscale_choropleth` and
`gen_spectral_choropleth`. Both these scripts take the same arguments, 
identified with specific flags:

 . `-b` - bottom value in the choropleth.
 . `-t` - top value in the choropleth.
 . `-c` - number of colour classes to generate.
 . `-o` - path to the resulting SLD file.
 
 Example:
 
 `gen_spectral_choropleth -b 10 -t 50 -c 20 -o style.sld`

Licence
-------------------------------------------------------------------------------

This programme is released under the [EUPL 1.1 licence](https://joinup.ec.europa.eu/community/eupl/og_page/introduction-eupl-licence). For full details please consult the LICENCE file.

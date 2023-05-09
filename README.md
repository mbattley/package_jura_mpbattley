# rv_curve_jura package

### JURA IV python example, May 09 2023

This package allows you to create a radial velocity plot of a star orbitied by a planet

### Usage instructions
```python
#import libraries
import numpy as np
import matplotlib.pylplot as plt
#import our rv_curve_class
from rv_curve_jura.rv_curve_module import rv_curve_class

#Create the instance
rv = rv_curve_class(t0=0., p=10., e=0.5, w=np.pi/3, k=10., t_init=0., t_end=25.)
# Use the plot method to create our plot
rv.plot()
'''
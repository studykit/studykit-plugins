# BeamNetwork.radii Property![](../images/TestTubeLarge.png)

Parent Object: [BeamNetwork](BeamNetwork.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/BeamNetwork.h>

## Description

The radii of the beams. Each radius is a double value. The radii define the radius of one end of the beam that corresponds to the same index in the beams array. The size of the array should be a multiple of 2, and equal to the length of the beams array.

## Syntax

* [Python](#Python)
* [C++](#C++)

"beamNetwork\_var" is a variable referencing a BeamNetwork object. |

"beamNetwork\_var" is a variable referencing a BeamNetwork object. ```` ``` #include <Volume/Volumetric/BeamNetwork.h>  // Get the value of the property. std::vector<double> propertyValue = beamNetwork_var->radii();  // Set the value of the property, where value_var is a double. bool returnValue = beamNetwork_var->radii(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type double.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
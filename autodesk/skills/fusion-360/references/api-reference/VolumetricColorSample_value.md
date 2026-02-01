# VolumetricColorSample.value Property![](../images/TestTubeLarge.png)

Parent Object: [VolumetricColorSample](VolumetricColorSample.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/VolumetricColorSample.h>

## Description

Gets the color value at the sample point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"volumetricColorSample\_var" is a variable referencing a VolumetricColorSample object. |

"volumetricColorSample\_var" is a variable referencing a VolumetricColorSample object. ```` ``` #include <Volume/Volumetric/VolumetricColorSample.h>  // Get the value of the property. Ptr<Color> propertyValue = volumetricColorSample_var->value(); ``` ```` |

## Property Value

This is a read only property whose value is a [Color](Color.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
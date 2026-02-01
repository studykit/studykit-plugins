# VolumetricCustomFeature.attributes Property![](../images/TestTubeLarge.png)

Parent Object: [VolumetricCustomFeature](VolumetricCustomFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VolumetricCustomFeature.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"volumetricCustomFeature\_var" is a variable referencing a VolumetricCustomFeature object. |

"volumetricCustomFeature\_var" is a variable referencing a VolumetricCustomFeature object. ```` ``` #include <Fusion/Features/VolumetricCustomFeature.h>  // Get the value of the property. Ptr<Attributes> propertyValue = volumetricCustomFeature_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
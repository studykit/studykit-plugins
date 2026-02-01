# GeometryGraphNodeProperty.name Property![](../images/TestTubeLarge.png)

Parent Object: [GeometryGraphNodeProperty](GeometryGraphNodeProperty.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/GeometryGraphNodeProperty.h>

## Description

Gets the internal name of the property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometryGraphNodeProperty\_var" is a variable referencing a GeometryGraphNodeProperty object. |

"geometryGraphNodeProperty\_var" is a variable referencing a GeometryGraphNodeProperty object. ```` ``` #include <Volume/Volumetric/GeometryGraphNodeProperty.h>  // Get the value of the property. string propertyValue = geometryGraphNodeProperty_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
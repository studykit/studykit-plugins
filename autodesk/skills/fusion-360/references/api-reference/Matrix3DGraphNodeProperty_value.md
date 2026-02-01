# Matrix3DGraphNodeProperty.value Property![](../images/TestTubeLarge.png)

Parent Object: [Matrix3DGraphNodeProperty](Matrix3DGraphNodeProperty.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/Matrix3DGraphNodeProperty.h>

## Description

Get or set the value of the property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3DGraphNodeProperty\_var" is a variable referencing a Matrix3DGraphNodeProperty object. |

"matrix3DGraphNodeProperty\_var" is a variable referencing a Matrix3DGraphNodeProperty object. ```` ``` #include <Volume/Volumetric/Matrix3DGraphNodeProperty.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = matrix3DGraphNodeProperty_var->value();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = matrix3DGraphNodeProperty_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
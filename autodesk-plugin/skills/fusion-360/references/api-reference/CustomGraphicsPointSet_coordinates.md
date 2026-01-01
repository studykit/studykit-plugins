# CustomGraphicsPointSet.coordinates Property

Parent Object: [CustomGraphicsPointSet](CustomGraphicsPointSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsPointSet.h>

## Description

Gets and sets the coordinates used to define the position of the custom graphics points. If no indexList is specified, every coordinate will be drawn using a custom graphics point,

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. |

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. ```` ``` #include <Fusion/Graphics/CustomGraphicsPointSet.h>  // Get the value of the property. Ptr<CustomGraphicsCoordinates> propertyValue = customGraphicsPointSet_var->coordinates();  // Set the value of the property, where value_var is a CustomGraphicsCoordinates. bool returnValue = customGraphicsPointSet_var->coordinates(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CustomGraphicsMesh.coordinates Property

Parent Object: [CustomGraphicsMesh](CustomGraphicsMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsMesh.h>

## Description

Gets and sets the coordinates associated with this CustomGraphicsMesh.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. |

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. ```` ``` #include <Fusion/Graphics/CustomGraphicsMesh.h>  // Get the value of the property. Ptr<CustomGraphicsCoordinates> propertyValue = customGraphicsMesh_var->coordinates();  // Set the value of the property, where value_var is a CustomGraphicsCoordinates. bool returnValue = customGraphicsMesh_var->coordinates(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
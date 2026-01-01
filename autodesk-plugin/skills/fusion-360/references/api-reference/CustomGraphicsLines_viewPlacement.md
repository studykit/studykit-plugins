# CustomGraphicsLines.viewPlacement Property

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

Gets and sets the graphics view placement being applied to this graphics entity. A CustomGraphicsViewPlacement object can be created using the static create method of the class. When assigned to a graphics entity the position of the graphics is defined relative to the view in 2D view space (pixels) rather than in 3D model space (centimeters).

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. |

"customGraphicsLines\_var" is a variable referencing a CustomGraphicsLines object. ```` ``` #include <Fusion/Graphics/CustomGraphicsLines.h>  // Get the value of the property. Ptr<CustomGraphicsViewPlacement> propertyValue = customGraphicsLines_var->viewPlacement();  // Set the value of the property, where value_var is a CustomGraphicsViewPlacement. bool returnValue = customGraphicsLines_var->viewPlacement(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsViewPlacement](CustomGraphicsViewPlacement.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
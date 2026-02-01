# CustomGraphicsText.viewScale Property

Parent Object: [CustomGraphicsText](CustomGraphicsText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsText.h>

## Description

Gets and sets the graphics view scale being applied to this graphics entity. A CustomGraphicsViewScale object can be created using the static create method of the class. When assigned to a graphics entity the size of the graphics entity is defined in view space (pixels) instead of model space (centimeters).

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. |

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. ```` ``` #include <Fusion/Graphics/CustomGraphicsText.h>  // Get the value of the property. Ptr<CustomGraphicsViewScale> propertyValue = customGraphicsText_var->viewScale();  // Set the value of the property, where value_var is a CustomGraphicsViewScale. bool returnValue = customGraphicsText_var->viewScale(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsViewScale](CustomGraphicsViewScale.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
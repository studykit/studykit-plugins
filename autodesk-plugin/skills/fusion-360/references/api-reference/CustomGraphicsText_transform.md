# CustomGraphicsText.transform Property

Parent Object: [CustomGraphicsText](CustomGraphicsText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsText.h>

## Description

Gets and sets the transform associated with the graphics entity. When a new graphics entity is created its default transform is an identity matrix which results in the graphics entity being displayed in model space using the original coordinate data used to define the entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. |

"customGraphicsText\_var" is a variable referencing a CustomGraphicsText object. ```` ``` #include <Fusion/Graphics/CustomGraphicsText.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = customGraphicsText_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = customGraphicsText_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
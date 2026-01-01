# CustomGraphicsGroup.transform Property

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Gets and sets the transform associated with the graphics entity. When a new graphics entity is created its default transform is an identity matrix which results in the graphics entity being displayed in model space using the original coordinate data used to define the entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. |

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. ```` ``` #include <Fusion/Graphics/CustomGraphicsGroup.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = customGraphicsGroup_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = customGraphicsGroup_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
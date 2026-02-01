# ProjectedTextureMapControl.transform Property

Parent Object: [ProjectedTextureMapControl](ProjectedTextureMapControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/ProjectedTextureMapControl.h>

## Description

Gets and sets the transform that defines the position and orientation of how the texture is projected onto the body. The Z axis of the transform corresponds to the axis that is specified in the user-interface and is the primary direction of the texture.

## Syntax

* [Python](#Python)
* [C++](#C++)

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object. |

"projectedTextureMapControl\_var" is a variable referencing a ProjectedTextureMapControl object. ```` ``` #include <Core/Materials/ProjectedTextureMapControl.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = projectedTextureMapControl_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = projectedTextureMapControl_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
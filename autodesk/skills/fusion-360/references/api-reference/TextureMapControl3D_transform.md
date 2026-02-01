# TextureMapControl3D.transform Property

Parent Object: [TextureMapControl3D](TextureMapControl3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/TextureMapControl3D.h>

## Description

Gets and sets the transform that defines the position and orientation of how the texture is applied to the body. For wood grain, the Z direction of the defined coordinate system is the direction of the grain.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textureMapControl3D\_var" is a variable referencing a TextureMapControl3D object. |

"textureMapControl3D\_var" is a variable referencing a TextureMapControl3D object. ```` ``` #include <Core/Materials/TextureMapControl3D.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = textureMapControl3D_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = textureMapControl3D_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
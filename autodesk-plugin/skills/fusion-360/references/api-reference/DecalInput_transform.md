# DecalInput.transform Property

Parent Object: [DecalInput](DecalInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/DecalInput.h>

## Description

Gets and sets the transform of the decal. This controls the position, rotation, scaling, and flipping. This is done by providing a 3D matrix that defines a 3D coordinate system in model space. The origin of the matrix defines the center of the decal and must lie somewhere on the first face. The Z-axis of the matrix should be the same as the normal of the face at the origin. The X and Y axes define the orientation of the decal and must be both perpendicular to the Z and each other. Reversing the direction of the X or Y axis will flip the decal in that direction. The magnitude of the X and Y axes controls the scale, and the scale can be non-uniform, meaning the length of the X and Y vectors do not need to be the same.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decalInput\_var" is a variable referencing a DecalInput object. |

"decalInput\_var" is a variable referencing a DecalInput object. ```` ``` #include <Fusion/Image/DecalInput.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = decalInput_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = decalInput_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
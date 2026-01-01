# Viewport.modelToViewSpaceTransform Property

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Returns a transformation matrix that defines the transform from model to viewport space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a Viewport object. |

"viewport\_var" is a variable referencing a Viewport object. ```` ``` #include <Core/Application/Viewport.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = viewport_var->modelToViewSpaceTransform(); ``` ```` |

## Property Value

This is a read only property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
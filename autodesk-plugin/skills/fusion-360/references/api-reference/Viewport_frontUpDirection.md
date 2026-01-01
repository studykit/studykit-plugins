# Viewport.frontUpDirection Property

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Returns the up direction of the front view as defined by the view cube.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a Viewport object. |

"viewport\_var" is a variable referencing a Viewport object. ```` ``` #include <Core/Application/Viewport.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = viewport_var->frontUpDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
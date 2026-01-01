# Circle2D.transformBy Method

Parent Object: [Circle2D](Circle2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle2D.h>

## Description

Transforms this curve in 2D space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle2D\_var" is a variable referencing a [Circle2D](Circle2D.htm) object.```` ``` returnValue = circle2D_var.transformBy(matrix) ``` ```` |

"circle2D\_var" is a variable referencing a [Circle2D](Circle2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Return true if the transform was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| matrix | [Matrix2D](Matrix2D.htm) | A 2D matrix that defines the transform to apply to the curve. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
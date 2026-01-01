# Vector2D.transformBy Method

Parent Object: [Vector2D](Vector2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Vector2D.h>

## Description

Transforms the vector by specifying a 2D transformation matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"vector2D\_var" is a variable referencing a [Vector2D](Vector2D.htm) object.```` ``` returnValue = vector2D_var.transformBy(matrix) ``` ```` |

"vector2D\_var" is a variable referencing a [Vector2D](Vector2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| matrix | [Matrix2D](Matrix2D.htm) | The Matrix2D object that defines the transformation. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
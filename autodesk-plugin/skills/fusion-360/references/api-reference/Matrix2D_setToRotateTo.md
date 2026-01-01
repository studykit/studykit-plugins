# Matrix2D.setToRotateTo Method

Parent Object: [Matrix2D](Matrix2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix2D.h>

## Description

Sets to the matrix of rotation that would align the 'from' vector with the 'to' vector.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix2D\_var" is a variable referencing a [Matrix2D](Matrix2D.htm) object.```` ``` returnValue = matrix2D_var.setToRotateTo(from, to) ``` ```` |

"matrix2D\_var" is a variable referencing a [Matrix2D](Matrix2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| from | [Vector2D](Vector2D.htm) | The from vector. |
| to | [Vector2D](Vector2D.htm) | The to vector. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
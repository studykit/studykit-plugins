# Matrix3D.setCell Method

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Sets the specified cell in the 4x4 matrix to the specified value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object.```` ``` returnValue = matrix3D_var.setCell(row, column, value) ``` ```` |

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| row | integer | The index of the row. The first row has in index of 0 |
| column | integer | The index of the column. The first column has an index of 0 |
| value | double | The new cell value. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
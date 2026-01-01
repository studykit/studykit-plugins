# Matrix3D.getCell Method

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Gets the value of the specified cell in the 4x4 matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object.```` ``` returnValue = matrix3D_var.getCell(row, column) ``` ```` |

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| double | The cell value at [row][column]. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| row | integer | The index of the row. The first row has in index of 0 |
| column | integer | The index of the column. The first column has an index of 0 |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
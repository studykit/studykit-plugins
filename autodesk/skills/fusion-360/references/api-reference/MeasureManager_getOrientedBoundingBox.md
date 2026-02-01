# MeasureManager.getOrientedBoundingBox Method

Parent Object: [MeasureManager](MeasureManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MeasureManager.h>

## Description

Calculates an oriented bounding box for the input geometry. The bounding box is tight fitting to the input geometry and is particularly useful when you want to calculate a bounding box that is not oriented to be parallel to the model x-y-z plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"measureManager\_var" is a variable referencing a [MeasureManager](MeasureManager.htm) object.```` ``` returnValue = measureManager_var.getOrientedBoundingBox(geometry, lengthVector, widthVector) ``` ```` |

"measureManager\_var" is a variable referencing a [MeasureManager](MeasureManager.htm) object.  ```` ``` #include <Core/Application/MeasureManager.h>  returnValue = measureManager_var->getOrientedBoundingBox(geometry, lengthVector, widthVector); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OrientedBoundingBox3D](OrientedBoundingBox3D.htm) | Returns an OrientedBoundingBox3D object which provides the information that defines an oriented bounding box. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometry | [Base](Base.htm) | The geometry to calculate the bounding box for. This can be any of the B-Rep related entities. |
| lengthVector | [Vector3D](Vector3D.htm) | The direction the length of the oriented bounding box will be measured in. The magnitude of the vector is ignored and only the direction is used. |
| widthVector | [Vector3D](Vector3D.htm) | The direction the width of the oriented bounding box will be measured in. The magnitude of the vector is ignored and only the direction is used. This must be perpendicular to the length vector. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Measure Sample](MeasureSample_Sample.htm) | Measure related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
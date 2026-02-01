# Ellipse3D.getData Method

Parent Object: [Ellipse3D](Ellipse3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse3D.h>

## Description

Gets all of the data defining the ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipse3D\_var" is a variable referencing an [Ellipse3D](Ellipse3D.htm) object. |

```` ```  #include <Core/Geometry/Ellipse3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The output center point of the ellipse. |
| normal | [Vector3D](Vector3D.htm) | The output normal vector of the ellipse. |
| majorAxis | [Vector3D](Vector3D.htm) | The output major axis of the ellipse |
| majorRadius | double | The output major radius of the of the ellipse. |
| minorRadius | double | The output minor radius of the of the ellipse. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
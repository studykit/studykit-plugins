# Ellipse2D.getData Method

Parent Object: [Ellipse2D](Ellipse2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse2D.h>

## Description

Gets all of the data defining the ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipse2D\_var" is a variable referencing an [Ellipse2D](Ellipse2D.htm) object. |

```` ```  #include <Core/Geometry/Ellipse2D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point2D](Point2D.htm) | The output center point of the ellipse. |
| majorAxis | [Vector2D](Vector2D.htm) | The output major axis of the ellipse. |
| majorRadius | double | The output major radius of the of the ellipse. |
| minorRadius | double | The output minor radius of the of the ellipse. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
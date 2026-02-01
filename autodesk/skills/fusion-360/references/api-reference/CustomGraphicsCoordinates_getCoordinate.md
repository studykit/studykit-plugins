# CustomGraphicsCoordinates.getCoordinate Method

Parent Object: [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCoordinates.h>

## Description

Gets the coordinate at the specified index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object.```` ``` returnValue = customGraphicsCoordinates_var.getCoordinate(index) ``` ```` |

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point3D](Point3D.htm) | Returns the coordinate as a Point3D object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the coordinate to return. The first coordinate has an index of 0. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
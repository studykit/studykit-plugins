# CustomGraphicsCoordinates.setCoordinate Method

Parent Object: [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCoordinates.h>

## Description

Sets the coordinate at the specified index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object.```` ``` returnValue = customGraphicsCoordinates_var.setCoordinate(index, coordinate) ``` ```` |

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the coordinate was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the coordinate to set. The first coordinate has an index of 0. |
| coordinate | [Point3D](Point3D.htm) | The coordinate value as a Point3D object. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
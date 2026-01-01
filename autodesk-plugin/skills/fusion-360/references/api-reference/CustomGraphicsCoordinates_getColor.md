# CustomGraphicsCoordinates.getColor Method

Parent Object: [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCoordinates.h>

## Description

Gets the color assigned to the coordinate at the specified index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object.```` ``` returnValue = customGraphicsCoordinates_var.getColor(index) ``` ```` |

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Color](Color.htm) | Returns the color associated with the index. Can also return null in the case where there is no color assigned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the color to return. The first color has an index of 0. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
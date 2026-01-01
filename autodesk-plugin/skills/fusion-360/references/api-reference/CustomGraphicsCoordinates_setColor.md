# CustomGraphicsCoordinates.setColor Method

Parent Object: [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCoordinates.h>

## Description

Sets the color of the coordinate at the specified index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object.```` ``` returnValue = customGraphicsCoordinates_var.setColor(index, color) ``` ```` |

"customGraphicsCoordinates\_var" is a variable referencing a [CustomGraphicsCoordinates](CustomGraphicsCoordinates.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the color was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the coordinate to set. The first coordinate has an index of 0. |
| color | [Color](Color.htm) | The color value as a Color object. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
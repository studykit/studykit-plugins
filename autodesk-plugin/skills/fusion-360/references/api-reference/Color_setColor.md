# Color.setColor Method

Parent Object: [Color](Color.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Color.h>

## Description

Sets all of the color information.

## Syntax

* [Python](#Python)
* [C++](#C++)

"color\_var" is a variable referencing a [Color](Color.htm) object.```` ``` returnValue = color_var.setColor(red, green, blue, opacity) ``` ```` |

"color\_var" is a variable referencing a [Color](Color.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the color information was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| red | short | The red component of the color. The value can be 0 to 255. |
| green | short | The green component of the color. The value can be 0 to 255. |
| blue | short | The blue component of the color. The value can be 0 to 255. |
| opacity | short | The opacity of the color. The value can be 0 to 255. A value of 255 indicates it is completely opaque. Depending on where the color is used, the opacity value may be ignored. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
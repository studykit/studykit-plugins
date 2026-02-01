# Color.getColor Method

Parent Object: [Color](Color.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Color.h>

## Description

Gets all of the information defining this color.

## Syntax

* [Python](#Python)
* [C++](#C++)

"color\_var" is a variable referencing a [Color](Color.htm) object. |

```` ```  #include <Core/Application/Color.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if getting the color information was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| red | short | The red component of the color. The value can be 0 to 255. |
| green | short | The green component of the color. The value can be 0 to 255. |
| blue | short | The blue component of the color. The value can be 0 to 255. |
| opacity | short | The opacity of the color. The value can be 0 to 255. A value of 255 indicates it is completely opaque. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
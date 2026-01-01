# TextCommandPalette.setMaximumSize Method

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Sets the maximum size of the palette. The user cannot resize it to be larger than this size. This does not change the current size of the palette unless the palette is already larger than this size.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.```` ``` returnValue = textCommandPalette_var.setMaximumSize(width, height) ``` ```` |

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.  ```` ``` #include <Core/UserInterface/TextCommandPalette.h>  returnValue = textCommandPalette_var->setMaximumSize(width, height); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the maximum size was succesful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | integer | Specifies the maximum width of the palette. |
| height | integer | Specifies the maximum height of the palette. |

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
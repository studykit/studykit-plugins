# TextCommandPalette.deleteMe Method

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Deletes this palette. Fusion native palettes cannot be deleted. Use the isNative property to determine if this is a native or API created palette.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.```` ``` returnValue = textCommandPalette_var.deleteMe() ``` ```` |

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
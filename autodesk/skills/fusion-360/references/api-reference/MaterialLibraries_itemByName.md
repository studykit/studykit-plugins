# MaterialLibraries.itemByName Method

Parent Object: [MaterialLibraries](MaterialLibraries.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibraries.h>

## Description

Returns the specified Material Library using the name as seen in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibraries\_var" is a variable referencing a [MaterialLibraries](MaterialLibraries.htm) object.```` ``` returnValue = materialLibraries_var.itemByName(name) ``` ```` |

"materialLibraries\_var" is a variable referencing a [MaterialLibraries](MaterialLibraries.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MaterialLibrary](MaterialLibrary.htm) | Returns the specified material library or null if there's no match on the name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the library to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
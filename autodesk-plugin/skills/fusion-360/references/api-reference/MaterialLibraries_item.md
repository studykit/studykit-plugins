# MaterialLibraries.item Method

Parent Object: [MaterialLibraries](MaterialLibraries.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibraries.h>

## Description

Method that returns the specified Material Library using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibraries\_var" is a variable referencing a [MaterialLibraries](MaterialLibraries.htm) object.```` ``` returnValue = materialLibraries_var.item(index) ``` ```` |

"materialLibraries\_var" is a variable referencing a [MaterialLibraries](MaterialLibraries.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MaterialLibrary](MaterialLibrary.htm) | Returns the specified material library or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the item within the collection. The first item has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
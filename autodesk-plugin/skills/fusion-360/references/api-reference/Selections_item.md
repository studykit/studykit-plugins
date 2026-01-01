# Selections.item Method

Parent Object: [Selections](Selections.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selections.h>

## Description

Returns the specified selection using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selections\_var" is a variable referencing a [Selections](Selections.htm) object.```` ``` returnValue = selections_var.item(index) ``` ```` |

"selections\_var" is a variable referencing a [Selections](Selections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Selection](Selection.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
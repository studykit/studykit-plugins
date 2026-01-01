# Toolbars.item Method

Parent Object: [Toolbars](Toolbars.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbars.h>

## Description

Returns the specified toolbar using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbars\_var" is a variable referencing a [Toolbars](Toolbars.htm) object.```` ``` returnValue = toolbars_var.item(index) ``` ```` |

"toolbars\_var" is a variable referencing a [Toolbars](Toolbars.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Toolbar](Toolbar.htm) | Returns the specified item or null if an invalid index was specified. |

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
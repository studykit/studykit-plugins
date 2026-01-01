# SelectionCommandInput.selection Method

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Returns the selection at the specified index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object.```` ``` returnValue = selectionCommandInput_var.selection(index) ``` ```` |

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Selection](Selection.htm) | Returns the Selection at the specified index, or null on error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the selection to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
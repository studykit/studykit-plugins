# SelectionCommandInput.addSelectionFilter Method

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Adds an additional filter to the existing filter list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object.```` ``` returnValue = selectionCommandInput_var.addSelectionFilter(filter) ``` ```` |

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the filter was added successfully. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filter | string | The name of a selection filter to add. The valid list of selection filters can be found here: [Selection Filters](SelectionFilters_UM.htm). |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Operations.item Method

Parent Object: [Operations](Operations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operations.h>

## Description

Function that returns the specified operation using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operations\_var" is a variable referencing an [Operations](Operations.htm) object.```` ``` returnValue = operations_var.item(index) ``` ```` |

"operations\_var" is a variable referencing an [Operations](Operations.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Operation](Operation.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Setup Sheets API Sample](GenerateSetupSheets_Sample_Sample.htm) | Demonstrates generating the setup sheets for an existing toolpath.. |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
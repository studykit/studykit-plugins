# Setups.item Method

Parent Object: [Setups](Setups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setups.h>

## Description

Function that returns the specified setup using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setups\_var" is a variable referencing a [Setups](Setups.htm) object.```` ``` returnValue = setups_var.item(index) ``` ```` |

"setups\_var" is a variable referencing a [Setups](Setups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Setup](Setup.htm) | Returns the specified item or null if an invalid index was specified. |

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
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
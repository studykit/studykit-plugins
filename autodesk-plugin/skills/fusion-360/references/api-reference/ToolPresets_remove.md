# ToolPresets.remove Method

Parent Object: [ToolPresets](ToolPresets.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPresets.h>

## Description

Remove Preset by index from the owning Tool.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPresets\_var" is a variable referencing a [ToolPresets](ToolPresets.htm) object.```` ``` returnValue = toolPresets_var.remove(index) ``` ```` |

"toolPresets\_var" is a variable referencing a [ToolPresets](ToolPresets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true for successful deletion, false otherwise |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | Index of the Preset in the Tool that should be removed. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ToolPresets.item Method

Parent Object: [ToolPresets](ToolPresets.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPresets.h>

## Description

Get Preset by index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPresets\_var" is a variable referencing a [ToolPresets](ToolPresets.htm) object.```` ``` returnValue = toolPresets_var.item(index) ``` ```` |

"toolPresets\_var" is a variable referencing a [ToolPresets](ToolPresets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolPreset](ToolPreset.htm) | Returns Preset at by given index, null otherwise |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | Index of the Preset in the owning Tool that should be returned. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
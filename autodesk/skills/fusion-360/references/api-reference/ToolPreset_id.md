# ToolPreset.id Property

Parent Object: [ToolPreset](ToolPreset.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPreset.h>

## Description

Gets and sets the identifier of that Preset. The id can be used to select a Preset for a Operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPreset\_var" is a variable referencing a ToolPreset object. |

"toolPreset\_var" is a variable referencing a ToolPreset object. ```` ``` #include <Cam/Tools/ToolPreset.h>  // Get the value of the property. string propertyValue = toolPreset_var->id();  // Set the value of the property, where value_var is a string. bool returnValue = toolPreset_var->id(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
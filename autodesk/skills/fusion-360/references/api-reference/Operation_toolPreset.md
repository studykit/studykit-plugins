# Operation.toolPreset Property

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

Get or set the tool preset to be used. Must be a valid preset of the already assigned tool. Returns null if the operation has no tool or preset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an Operation object. |

"operation\_var" is a variable referencing an Operation object. ```` ``` #include <Cam/Operations/Operation.h>  // Get the value of the property. Ptr<ToolPreset> propertyValue = operation_var->toolPreset();  // Set the value of the property, where value_var is a ToolPreset. bool returnValue = operation_var->toolPreset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ToolPreset](ToolPreset.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
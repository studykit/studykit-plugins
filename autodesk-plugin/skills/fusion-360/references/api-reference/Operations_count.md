# Operations.count Property

Parent Object: [Operations](Operations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operations.h>

## Description

The number of items in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operations\_var" is a variable referencing an Operations object. |

"operations\_var" is a variable referencing an Operations object. ```` ``` #include <Cam/Operations/Operations.h>  // Get the value of the property. uinteger propertyValue = operations_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
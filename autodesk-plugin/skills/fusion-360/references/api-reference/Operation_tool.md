# Operation.tool Property

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

Get or set the tool for this operation. The document's tool library will be updated accordingly. The tool instance returned is a copy and therefore is not referenced by the operation. To change the tool of the operation, the new tool must be assigned to the operation. Setting a tool will override the current preset and will fall back to the default preset of the new tool.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an Operation object. |

"operation\_var" is a variable referencing an Operation object. ```` ``` #include <Cam/Operations/Operation.h>  // Get the value of the property. Ptr<Tool> propertyValue = operation_var->tool();  // Set the value of the property, where value_var is a Tool. bool returnValue = operation_var->tool(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Tool](Tool.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
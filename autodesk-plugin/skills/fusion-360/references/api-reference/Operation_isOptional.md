# Operation.isOptional Property

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

Gets and sets the "Optional" property value of the operation. Gets/sets true if the operation is optional.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an Operation object. |

"operation\_var" is a variable referencing an Operation object. ```` ``` #include <Cam/Operations/Operation.h>  // Get the value of the property. boolean propertyValue = operation_var->isOptional();  // Set the value of the property, where value_var is a boolean. bool returnValue = operation_var->isOptional(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
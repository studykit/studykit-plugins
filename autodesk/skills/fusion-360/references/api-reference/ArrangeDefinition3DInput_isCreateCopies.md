# ArrangeDefinition3DInput.isCreateCopies Property

Parent Object: [ArrangeDefinition3DInput](ArrangeDefinition3DInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition3DInput.h>

## Description

Gets and set if the original components will be moved or copied to create the arrangement. This defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinition3DInput\_var" is a variable referencing an ArrangeDefinition3DInput object. |

"arrangeDefinition3DInput\_var" is a variable referencing an ArrangeDefinition3DInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinition3DInput.h>  // Get the value of the property. boolean propertyValue = arrangeDefinition3DInput_var->isCreateCopies();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeDefinition3DInput_var->isCreateCopies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
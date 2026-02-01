# ArrangeDefinitionInput.isCreateCopies Property

Parent Object: [ArrangeDefinitionInput](ArrangeDefinitionInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinitionInput.h>

## Description

Gets and set if the original components will be moved or copied to create the arrangement. This defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinitionInput\_var" is a variable referencing an ArrangeDefinitionInput object. |

"arrangeDefinitionInput\_var" is a variable referencing an ArrangeDefinitionInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinitionInput.h>  // Get the value of the property. boolean propertyValue = arrangeDefinitionInput_var->isCreateCopies();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeDefinitionInput_var->isCreateCopies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
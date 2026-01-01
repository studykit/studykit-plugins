# ArrangeDefinitionInput.objectType Property

Parent Object: [ArrangeDefinitionInput](ArrangeDefinitionInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinitionInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinitionInput\_var" is a variable referencing an ArrangeDefinitionInput object.  ```` ``` # Get the value of the property. propertyValue = arrangeDefinitionInput_var.objectType ``` ```` |

"arrangeDefinitionInput\_var" is a variable referencing an ArrangeDefinitionInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinitionInput.h>  // Get the value of the property. string propertyValue = arrangeDefinitionInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
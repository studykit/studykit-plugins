# ArrangeDefinition3DInput.objectType Property

Parent Object: [ArrangeDefinition3DInput](ArrangeDefinition3DInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition3DInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinition3DInput\_var" is a variable referencing an ArrangeDefinition3DInput object.  ```` ``` # Get the value of the property. propertyValue = arrangeDefinition3DInput_var.objectType ``` ```` |

"arrangeDefinition3DInput\_var" is a variable referencing an ArrangeDefinition3DInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinition3DInput.h>  // Get the value of the property. string propertyValue = arrangeDefinition3DInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# JointInput.objectType Property

Parent Object: [JointInput](JointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointInput\_var" is a variable referencing a JointInput object.  ```` ``` # Get the value of the property. propertyValue = jointInput_var.objectType ``` ```` |

"jointInput\_var" is a variable referencing a JointInput object. ```` ``` #include <Fusion/Components/JointInput.h>  // Get the value of the property. string propertyValue = jointInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
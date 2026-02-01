# AsBuiltJointInput.objectType Property

Parent Object: [AsBuiltJointInput](AsBuiltJointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointInput\_var" is a variable referencing an AsBuiltJointInput object.  ```` ``` # Get the value of the property. propertyValue = asBuiltJointInput_var.objectType ``` ```` |

"asBuiltJointInput\_var" is a variable referencing an AsBuiltJointInput object. ```` ``` #include <Fusion/Components/AsBuiltJointInput.h>  // Get the value of the property. string propertyValue = asBuiltJointInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
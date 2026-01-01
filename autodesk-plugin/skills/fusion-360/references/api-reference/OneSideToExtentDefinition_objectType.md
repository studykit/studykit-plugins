# OneSideToExtentDefinition.objectType Property

Parent Object: [OneSideToExtentDefinition](OneSideToExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OneSideToExtentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = oneSideToExtentDefinition_var.objectType ``` ```` |

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object. ```` ``` #include <Fusion/Features/OneSideToExtentDefinition.h>  // Get the value of the property. string propertyValue = oneSideToExtentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
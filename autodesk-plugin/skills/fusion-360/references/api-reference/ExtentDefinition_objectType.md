# ExtentDefinition.objectType Property

Parent Object: [ExtentDefinition](ExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extentDefinition\_var" is a variable referencing an ExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = extentDefinition_var.objectType ``` ```` |

"extentDefinition\_var" is a variable referencing an ExtentDefinition object. ```` ``` #include <Fusion/Features/ExtentDefinition.h>  // Get the value of the property. string propertyValue = extentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
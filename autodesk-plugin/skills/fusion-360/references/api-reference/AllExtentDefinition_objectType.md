# AllExtentDefinition.objectType Property

Parent Object: [AllExtentDefinition](AllExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AllExtentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"allExtentDefinition\_var" is a variable referencing an AllExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = allExtentDefinition_var.objectType ``` ```` |

"allExtentDefinition\_var" is a variable referencing an AllExtentDefinition object. ```` ``` #include <Fusion/Features/AllExtentDefinition.h>  // Get the value of the property. string propertyValue = allExtentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
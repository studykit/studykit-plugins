# Analyses.objectType Property

Parent Object: [Analyses](Analyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analyses.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analyses\_var" is a variable referencing an Analyses object.  ```` ``` # Get the value of the property. propertyValue = analyses_var.objectType ``` ```` |

"analyses\_var" is a variable referencing an Analyses object. ```` ``` #include <Fusion/Fusion/Analyses.h>  // Get the value of the property. string propertyValue = analyses_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
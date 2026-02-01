# RipFeatures.objectType Property

Parent Object: [RipFeatures](RipFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatures\_var" is a variable referencing a RipFeatures object.  ```` ``` # Get the value of the property. propertyValue = ripFeatures_var.objectType ``` ```` |

"ripFeatures\_var" is a variable referencing a RipFeatures object. ```` ``` #include <Fusion/SheetMetal/RipFeatures.h>  // Get the value of the property. string propertyValue = ripFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
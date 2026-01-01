# FlangeFeatures.objectType Property

Parent Object: [FlangeFeatures](FlangeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flangeFeatures\_var" is a variable referencing a FlangeFeatures object.  ```` ``` # Get the value of the property. propertyValue = flangeFeatures_var.objectType ``` ```` |

"flangeFeatures\_var" is a variable referencing a FlangeFeatures object. ```` ``` #include <Fusion/SheetMetal/FlangeFeatures.h>  // Get the value of the property. string propertyValue = flangeFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
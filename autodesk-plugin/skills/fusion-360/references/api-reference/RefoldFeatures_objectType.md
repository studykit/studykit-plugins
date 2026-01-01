# RefoldFeatures.objectType Property

Parent Object: [RefoldFeatures](RefoldFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RefoldFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"refoldFeatures\_var" is a variable referencing a RefoldFeatures object.  ```` ``` # Get the value of the property. propertyValue = refoldFeatures_var.objectType ``` ```` |

"refoldFeatures\_var" is a variable referencing a RefoldFeatures object. ```` ``` #include <Fusion/SheetMetal/RefoldFeatures.h>  // Get the value of the property. string propertyValue = refoldFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
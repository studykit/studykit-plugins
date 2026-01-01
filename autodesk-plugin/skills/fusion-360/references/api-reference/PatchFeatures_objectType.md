# PatchFeatures.objectType Property

Parent Object: [PatchFeatures](PatchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatures\_var" is a variable referencing a PatchFeatures object.  ```` ``` # Get the value of the property. propertyValue = patchFeatures_var.objectType ``` ```` |

"patchFeatures\_var" is a variable referencing a PatchFeatures object. ```` ``` #include <Fusion/Features/PatchFeatures.h>  // Get the value of the property. string propertyValue = patchFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
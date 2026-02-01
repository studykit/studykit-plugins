# ExtendFeatures.objectType Property

Parent Object: [ExtendFeatures](ExtendFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatures\_var" is a variable referencing an ExtendFeatures object.  ```` ``` # Get the value of the property. propertyValue = extendFeatures_var.objectType ``` ```` |

"extendFeatures\_var" is a variable referencing an ExtendFeatures object. ```` ``` #include <Fusion/Features/ExtendFeatures.h>  // Get the value of the property. string propertyValue = extendFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
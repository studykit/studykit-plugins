# FilletFeatures.objectType Property

Parent Object: [FilletFeatures](FilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatures\_var" is a variable referencing a FilletFeatures object.  ```` ``` # Get the value of the property. propertyValue = filletFeatures_var.objectType ``` ```` |

"filletFeatures\_var" is a variable referencing a FilletFeatures object. ```` ``` #include <Fusion/Features/FilletFeatures.h>  // Get the value of the property. string propertyValue = filletFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
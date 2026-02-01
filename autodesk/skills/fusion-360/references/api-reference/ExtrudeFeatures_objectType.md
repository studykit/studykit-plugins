# ExtrudeFeatures.objectType Property

Parent Object: [ExtrudeFeatures](ExtrudeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatures\_var" is a variable referencing an ExtrudeFeatures object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeatures_var.objectType ``` ```` |

"extrudeFeatures\_var" is a variable referencing an ExtrudeFeatures object. ```` ``` #include <Fusion/Features/ExtrudeFeatures.h>  // Get the value of the property. string propertyValue = extrudeFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# RevolveFeatures.objectType Property

Parent Object: [RevolveFeatures](RevolveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatures\_var" is a variable referencing a RevolveFeatures object.  ```` ``` # Get the value of the property. propertyValue = revolveFeatures_var.objectType ``` ```` |

"revolveFeatures\_var" is a variable referencing a RevolveFeatures object. ```` ``` #include <Fusion/Features/RevolveFeatures.h>  // Get the value of the property. string propertyValue = revolveFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
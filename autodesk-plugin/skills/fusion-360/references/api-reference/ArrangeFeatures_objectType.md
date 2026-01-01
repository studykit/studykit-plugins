# ArrangeFeatures.objectType Property

Parent Object: [ArrangeFeatures](ArrangeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatures\_var" is a variable referencing an ArrangeFeatures object.  ```` ``` # Get the value of the property. propertyValue = arrangeFeatures_var.objectType ``` ```` |

"arrangeFeatures\_var" is a variable referencing an ArrangeFeatures object. ```` ``` #include <Fusion/Arrange/ArrangeFeatures.h>  // Get the value of the property. string propertyValue = arrangeFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
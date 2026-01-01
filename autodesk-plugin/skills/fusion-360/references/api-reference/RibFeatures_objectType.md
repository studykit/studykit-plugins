# RibFeatures.objectType Property

Parent Object: [RibFeatures](RibFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeatures\_var" is a variable referencing a RibFeatures object.  ```` ``` # Get the value of the property. propertyValue = ribFeatures_var.objectType ``` ```` |

"ribFeatures\_var" is a variable referencing a RibFeatures object. ```` ``` #include <Fusion/Features/RibFeatures.h>  // Get the value of the property. string propertyValue = ribFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
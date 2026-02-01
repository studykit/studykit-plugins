# TorusFeatures.objectType Property

Parent Object: [TorusFeatures](TorusFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TorusFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torusFeatures\_var" is a variable referencing a TorusFeatures object.  ```` ``` # Get the value of the property. propertyValue = torusFeatures_var.objectType ``` ```` |

"torusFeatures\_var" is a variable referencing a TorusFeatures object. ```` ``` #include <Fusion/Features/TorusFeatures.h>  // Get the value of the property. string propertyValue = torusFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
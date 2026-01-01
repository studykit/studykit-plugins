# ThickenFeatures.objectType Property

Parent Object: [ThickenFeatures](ThickenFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatures\_var" is a variable referencing a ThickenFeatures object.  ```` ``` # Get the value of the property. propertyValue = thickenFeatures_var.objectType ``` ```` |

"thickenFeatures\_var" is a variable referencing a ThickenFeatures object. ```` ``` #include <Fusion/Features/ThickenFeatures.h>  // Get the value of the property. string propertyValue = thickenFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
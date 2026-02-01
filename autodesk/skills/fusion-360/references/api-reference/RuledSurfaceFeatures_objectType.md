# RuledSurfaceFeatures.objectType Property

Parent Object: [RuledSurfaceFeatures](RuledSurfaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatures\_var" is a variable referencing a RuledSurfaceFeatures object.  ```` ``` # Get the value of the property. propertyValue = ruledSurfaceFeatures_var.objectType ``` ```` |

"ruledSurfaceFeatures\_var" is a variable referencing a RuledSurfaceFeatures object. ```` ``` #include <Fusion/Features/RuledSurfaceFeatures.h>  // Get the value of the property. string propertyValue = ruledSurfaceFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
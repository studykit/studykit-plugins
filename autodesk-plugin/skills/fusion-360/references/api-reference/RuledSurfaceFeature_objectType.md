# RuledSurfaceFeature.objectType Property

Parent Object: [RuledSurfaceFeature](RuledSurfaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object.  ```` ``` # Get the value of the property. propertyValue = ruledSurfaceFeature_var.objectType ``` ```` |

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. ```` ``` #include <Fusion/Features/RuledSurfaceFeature.h>  // Get the value of the property. string propertyValue = ruledSurfaceFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
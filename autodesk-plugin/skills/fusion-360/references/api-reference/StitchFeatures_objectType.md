# StitchFeatures.objectType Property

Parent Object: [StitchFeatures](StitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatures\_var" is a variable referencing a StitchFeatures object.  ```` ``` # Get the value of the property. propertyValue = stitchFeatures_var.objectType ``` ```` |

"stitchFeatures\_var" is a variable referencing a StitchFeatures object. ```` ``` #include <Fusion/Features/StitchFeatures.h>  // Get the value of the property. string propertyValue = stitchFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
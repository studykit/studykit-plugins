# MirrorFeatures.objectType Property

Parent Object: [MirrorFeatures](MirrorFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatures\_var" is a variable referencing a MirrorFeatures object.  ```` ``` # Get the value of the property. propertyValue = mirrorFeatures_var.objectType ``` ```` |

"mirrorFeatures\_var" is a variable referencing a MirrorFeatures object. ```` ``` #include <Fusion/Features/MirrorFeatures.h>  // Get the value of the property. string propertyValue = mirrorFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
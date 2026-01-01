# SilhouetteSplitFeatures.objectType Property

Parent Object: [SilhouetteSplitFeatures](SilhouetteSplitFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatures\_var" is a variable referencing a SilhouetteSplitFeatures object.  ```` ``` # Get the value of the property. propertyValue = silhouetteSplitFeatures_var.objectType ``` ```` |

"silhouetteSplitFeatures\_var" is a variable referencing a SilhouetteSplitFeatures object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeatures.h>  // Get the value of the property. string propertyValue = silhouetteSplitFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
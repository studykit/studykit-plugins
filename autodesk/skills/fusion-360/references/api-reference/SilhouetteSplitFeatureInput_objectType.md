# SilhouetteSplitFeatureInput.objectType Property

Parent Object: [SilhouetteSplitFeatureInput](SilhouetteSplitFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = silhouetteSplitFeatureInput_var.objectType ``` ```` |

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeatureInput.h>  // Get the value of the property. string propertyValue = silhouetteSplitFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
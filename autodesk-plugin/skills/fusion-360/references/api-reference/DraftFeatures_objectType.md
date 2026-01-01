# DraftFeatures.objectType Property

Parent Object: [DraftFeatures](DraftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatures\_var" is a variable referencing a DraftFeatures object.  ```` ``` # Get the value of the property. propertyValue = draftFeatures_var.objectType ``` ```` |

"draftFeatures\_var" is a variable referencing a DraftFeatures object. ```` ``` #include <Fusion/Features/DraftFeatures.h>  // Get the value of the property. string propertyValue = draftFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
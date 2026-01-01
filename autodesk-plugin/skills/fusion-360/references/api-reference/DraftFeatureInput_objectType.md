# DraftFeatureInput.objectType Property

Parent Object: [DraftFeatureInput](DraftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = draftFeatureInput_var.objectType ``` ```` |

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. ```` ``` #include <Fusion/Features/DraftFeatureInput.h>  // Get the value of the property. string propertyValue = draftFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
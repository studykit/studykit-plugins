# FeatureList.objectType Property

Parent Object: [FeatureList](FeatureList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FeatureList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"featureList\_var" is a variable referencing a FeatureList object.  ```` ``` # Get the value of the property. propertyValue = featureList_var.objectType ``` ```` |

"featureList\_var" is a variable referencing a FeatureList object. ```` ``` #include <Fusion/Features/FeatureList.h>  // Get the value of the property. string propertyValue = featureList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
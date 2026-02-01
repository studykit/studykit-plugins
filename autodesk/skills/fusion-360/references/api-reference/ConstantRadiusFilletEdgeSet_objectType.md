# ConstantRadiusFilletEdgeSet.objectType Property

Parent Object: [ConstantRadiusFilletEdgeSet](ConstantRadiusFilletEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ConstantRadiusFilletEdgeSet.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constantRadiusFilletEdgeSet\_var" is a variable referencing a ConstantRadiusFilletEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = constantRadiusFilletEdgeSet_var.objectType ``` ```` |

"constantRadiusFilletEdgeSet\_var" is a variable referencing a ConstantRadiusFilletEdgeSet object. ```` ``` #include <Fusion/Features/ConstantRadiusFilletEdgeSet.h>  // Get the value of the property. string propertyValue = constantRadiusFilletEdgeSet_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
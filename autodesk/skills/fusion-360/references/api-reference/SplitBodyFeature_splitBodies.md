# SplitBodyFeature.splitBodies Property

Parent Object: [SplitBodyFeature](SplitBodyFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeature.h>

## Description

Gets and sets the input solid or open bodies that are split.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object.  ```` ``` # Get the value of the property. propertyValue = splitBodyFeature_var.splitBodies  # Set the value of the property. splitBodyFeature_var.splitBodies = propertyValue ``` ```` |

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object. ```` ``` #include <Fusion/Features/SplitBodyFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = splitBodyFeature_var->splitBodies();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = splitBodyFeature_var->splitBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
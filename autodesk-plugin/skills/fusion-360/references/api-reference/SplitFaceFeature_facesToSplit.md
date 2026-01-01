# SplitFaceFeature.facesToSplit Property

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Gets and sets the faces to be split. The collection can contain one or more faces selected from solid and/or open bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = splitFaceFeature_var.facesToSplit  # Set the value of the property. splitFaceFeature_var.facesToSplit = propertyValue ``` ```` |

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object. ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = splitFaceFeature_var->facesToSplit();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = splitFaceFeature_var->facesToSplit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
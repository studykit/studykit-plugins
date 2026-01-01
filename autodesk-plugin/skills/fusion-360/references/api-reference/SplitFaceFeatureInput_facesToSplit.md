# SplitFaceFeatureInput.facesToSplit Property

Parent Object: [SplitFaceFeatureInput](SplitFaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatureInput.h>

## Description

Gets and sets the faces to be split. The collection can contain one or more faces selected from solid and/or open bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeatureInput\_var" is a variable referencing a SplitFaceFeatureInput object. |

"splitFaceFeatureInput\_var" is a variable referencing a SplitFaceFeatureInput object. ```` ``` #include <Fusion/Features/SplitFaceFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = splitFaceFeatureInput_var->facesToSplit();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = splitFaceFeatureInput_var->facesToSplit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
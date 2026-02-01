# SplitFaceFeature.splittingTool Property

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Gets the entity(s) that define the splitting tool(s). The splitting tool can consist of one or more of the following: BRepBody, ConstructionPlane, BRepFace, sketch curve that extends or can be extended beyond the extents of the face. To set the splitting tool, use one of the set methods to also define the split type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = splitFaceFeature_var.splittingTool ``` ```` |

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object. ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = splitFaceFeature_var->splittingTool(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
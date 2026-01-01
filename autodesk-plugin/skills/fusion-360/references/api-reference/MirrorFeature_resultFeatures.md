# MirrorFeature.resultFeatures Property

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Get the features that were created for this mirror. Returns null in the case where the feature is not parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. |

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. ```` ``` #include <Fusion/Features/MirrorFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = mirrorFeature_var->resultFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
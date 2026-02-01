# Features.splitFaceFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the SplitFace features within the component and supports the creation of new SplitFace features

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<SplitFaceFeatures> propertyValue = features_var->splitFaceFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [SplitFaceFeatures](SplitFaceFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [splitFaceFeatures.add](splitFaceFeatures_add_Sample.htm) | Demonstrates the splitFaceFeatures.add method by spliting a face with another intersecting face. |
| [Split Face Feature API Sample](SplitFaceFeatureSample_Sample.htm) | Demonstrates creating a new split face feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
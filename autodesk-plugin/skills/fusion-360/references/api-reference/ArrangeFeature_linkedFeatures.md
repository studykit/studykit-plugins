# ArrangeFeature.linkedFeatures Property

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. |

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. ```` ``` #include <Fusion/Arrange/ArrangeFeature.h>  // Get the value of the property. Ptr<FeatureList> propertyValue = arrangeFeature_var->linkedFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureList](FeatureList.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
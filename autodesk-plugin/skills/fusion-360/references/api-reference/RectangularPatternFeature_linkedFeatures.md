# RectangularPatternFeature.linkedFeatures Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. Ptr<FeatureList> propertyValue = rectangularPatternFeature_var->linkedFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureList](FeatureList.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
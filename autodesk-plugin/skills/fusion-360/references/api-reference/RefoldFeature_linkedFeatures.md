# RefoldFeature.linkedFeatures Property

Parent Object: [RefoldFeature](RefoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RefoldFeature.h>

## Description

Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"refoldFeature\_var" is a variable referencing a RefoldFeature object. |

"refoldFeature\_var" is a variable referencing a RefoldFeature object. ```` ``` #include <Fusion/SheetMetal/RefoldFeature.h>  // Get the value of the property. Ptr<FeatureList> propertyValue = refoldFeature_var->linkedFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureList](FeatureList.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
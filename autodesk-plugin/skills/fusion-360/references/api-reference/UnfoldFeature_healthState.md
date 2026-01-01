# UnfoldFeature.healthState Property

Parent Object: [UnfoldFeature](UnfoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/UnfoldFeature.h>

## Description

Returns the current health state of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object. |

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object. ```` ``` #include <Fusion/SheetMetal/UnfoldFeature.h>  // Get the value of the property. FeatureHealthStates propertyValue = unfoldFeature_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
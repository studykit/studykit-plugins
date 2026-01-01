# SplitFaceFeature.isSplittingToolExtended Property

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Gets whether or not the setting to automatically extend the splittingTool was set when the feature was created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = splitFaceFeature_var.isSplittingToolExtended ``` ```` |

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object. ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  // Get the value of the property. boolean propertyValue = splitFaceFeature_var->isSplittingToolExtended(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
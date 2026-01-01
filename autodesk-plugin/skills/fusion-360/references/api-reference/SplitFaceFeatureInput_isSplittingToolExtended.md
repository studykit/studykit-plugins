# SplitFaceFeatureInput.isSplittingToolExtended Property

Parent Object: [SplitFaceFeatureInput](SplitFaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatureInput.h>

## Description

Gets and sets whether or not the splittingTool is to be automatically extended (if possible) so as to completely intersect the facesToSplit.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeatureInput\_var" is a variable referencing a SplitFaceFeatureInput object. |

"splitFaceFeatureInput\_var" is a variable referencing a SplitFaceFeatureInput object. ```` ``` #include <Fusion/Features/SplitFaceFeatureInput.h>  // Get the value of the property. boolean propertyValue = splitFaceFeatureInput_var->isSplittingToolExtended();  // Set the value of the property, where value_var is a boolean. bool returnValue = splitFaceFeatureInput_var->isSplittingToolExtended(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SplitBodyFeatureInput.isSplittingToolExtended Property

Parent Object: [SplitBodyFeatureInput](SplitBodyFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeatureInput.h>

## Description

Gets and sets whether or not the splitting tool is to be automatically extended (if possible) so as to completely intersect the bodyToSplit.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeatureInput\_var" is a variable referencing a SplitBodyFeatureInput object. |

"splitBodyFeatureInput\_var" is a variable referencing a SplitBodyFeatureInput object. ```` ``` #include <Fusion/Features/SplitBodyFeatureInput.h>  // Get the value of the property. boolean propertyValue = splitBodyFeatureInput_var->isSplittingToolExtended();  // Set the value of the property, where value_var is a boolean. bool returnValue = splitBodyFeatureInput_var->isSplittingToolExtended(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
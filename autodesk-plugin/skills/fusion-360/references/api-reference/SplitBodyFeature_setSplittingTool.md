# SplitBodyFeature.setSplittingTool Method

Parent Object: [SplitBodyFeature](SplitBodyFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeature.h>

## Description

Sets the splitting tool used for the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeature\_var" is a variable referencing a [SplitBodyFeature](SplitBodyFeature.htm) object.```` ``` returnValue = splitBodyFeature_var.setSplittingTool(splittingTool, isSplittingToolExtended) ``` ```` |

"splitBodyFeature\_var" is a variable referencing a [SplitBodyFeature](SplitBodyFeature.htm) object.  ```` ``` #include <Fusion/Features/SplitBodyFeature.h>  returnValue = splitBodyFeature_var->setSplittingTool(splittingTool, isSplittingToolExtended); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| splittingTool | [Base](Base.htm) | Input entity that defines the splitting tool. The splitting tool is a single entity that can be either a solid body, open body, construction plane, face, or sketch curve that partially or fully intersects the body to split. |
| isSplittingToolExtended | boolean | A boolean value for setting whether or not the splittingTool is to be automatically extended (if possible) so as to completely intersect the facesToSplit. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
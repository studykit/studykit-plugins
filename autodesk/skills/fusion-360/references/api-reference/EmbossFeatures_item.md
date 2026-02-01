# EmbossFeatures.item Method![](../images/TestTubeLarge.png)

Parent Object: [EmbossFeatures](EmbossFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EmbossFeatures.h>

## Description

Function that returns the specified emboss feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"embossFeatures\_var" is a variable referencing an [EmbossFeatures](EmbossFeatures.htm) object.```` ``` returnValue = embossFeatures_var.item(index) ``` ```` |

"embossFeatures\_var" is a variable referencing an [EmbossFeatures](EmbossFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [EmbossFeature](EmbossFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
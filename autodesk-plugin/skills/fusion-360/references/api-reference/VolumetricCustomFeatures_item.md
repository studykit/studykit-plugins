# VolumetricCustomFeatures.item Method![](../images/TestTubeLarge.png)

Parent Object: [VolumetricCustomFeatures](VolumetricCustomFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VolumetricCustomFeatures.h>

## Description

Function that returns the specified item using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"volumetricCustomFeatures\_var" is a variable referencing a [VolumetricCustomFeatures](VolumetricCustomFeatures.htm) object.```` ``` returnValue = volumetricCustomFeatures_var.item(index) ``` ```` |

"volumetricCustomFeatures\_var" is a variable referencing a [VolumetricCustomFeatures](VolumetricCustomFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [VolumetricCustomFeature](VolumetricCustomFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
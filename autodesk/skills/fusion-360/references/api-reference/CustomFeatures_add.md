# CustomFeatures.add Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatures](CustomFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatures.h>

## Description

Creates a new custom feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatures\_var" is a variable referencing a [CustomFeatures](CustomFeatures.htm) object.```` ``` returnValue = customFeatures_var.add(input) ``` ```` |

"customFeatures\_var" is a variable referencing a [CustomFeatures](CustomFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomFeature](CustomFeature.htm) | Returns the newly created CustomFeature. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [CustomFeatureInput](CustomFeatureInput.htm) | The CustomFeatureInput object that defines the information needed to create a custom feature. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
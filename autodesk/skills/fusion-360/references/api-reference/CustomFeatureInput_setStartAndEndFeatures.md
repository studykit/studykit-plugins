# CustomFeatureInput.setStartAndEndFeatures Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureInput](CustomFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureInput.h>

## Description

Sets the start and end features that the custom feature will group. A "feature" in this case is an object that is visible in the timeline, such as modeling features, sketches, and construction geometry. The custom feature will group the input start and end features and all features between them in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureInput\_var" is a variable referencing a [CustomFeatureInput](CustomFeatureInput.htm) object.```` ``` returnValue = customFeatureInput_var.setStartAndEndFeatures(startFeature, endFeature) ``` ```` |

"customFeatureInput\_var" is a variable referencing a [CustomFeatureInput](CustomFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the start and end features was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startFeature | [Base](Base.htm) | The first feature in the timeline that the custom feature will group. |
| endFeature | [Base](Base.htm) | The last feature in the timeline that the custom feature will group. When creating a custom feature that contains a single feature, this can be the same feature as the startFeature argument. |

## Version

Introduced in version August 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CustomFeatures.createInput Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatures](CustomFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatures.h>

## Description

Creates a new input object that you use to define a custom feature. Creating an input object doesn't create the feature but provides a way to gather all of the input needed to create a custom feature. To create the custom feature, the fully defined input object is passed to the add method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatures\_var" is a variable referencing a [CustomFeatures](CustomFeatures.htm) object.```` ``` returnValue = customFeatures_var.createInput(definition) ``` ```` |

"customFeatures\_var" is a variable referencing a [CustomFeatures](CustomFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomFeatureInput](CustomFeatureInput.htm) | Returns the newly created CustomFeatureInput object or null in the case of invalid input. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| definition | [CustomFeatureDefinition](CustomFeatureDefinition.htm) | The CustomFeatureDefinition for the type of custom feature being created. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
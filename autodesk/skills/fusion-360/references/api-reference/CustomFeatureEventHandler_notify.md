# CustomFeatureEventHandler.notify Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureEventHandler](CustomFeatureEventHandler.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureEventHandler\_var" is a variable referencing a [CustomFeatureEventHandler](CustomFeatureEventHandler.htm) object.```` ``` returnValue = customFeatureEventHandler_var.notify(eventArgs) ``` ```` |

"customFeatureEventHandler\_var" is a variable referencing a [CustomFeatureEventHandler](CustomFeatureEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [CustomFeatureEventArgs](CustomFeatureEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CustomFeatureEvent.add Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureEvent](CustomFeatureEvent.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureEvent.h>

## Description

Add a handler to be notified when the file event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureEvent\_var" is a variable referencing a [CustomFeatureEvent](CustomFeatureEvent.htm) object.```` ``` returnValue = customFeatureEvent_var.add(handler) ``` ```` |

"customFeatureEvent\_var" is a variable referencing a [CustomFeatureEvent](CustomFeatureEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [CustomFeatureEventHandler](CustomFeatureEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
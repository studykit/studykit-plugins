# CustomFeatureEvent.sender Property![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureEvent](CustomFeatureEvent.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureEvent\_var" is a variable referencing a CustomFeatureEvent object. |

"customFeatureEvent\_var" is a variable referencing a CustomFeatureEvent object. ```` ``` #include <Fusion/Features/CustomFeatureEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = customFeatureEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
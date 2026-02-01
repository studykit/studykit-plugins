# MultiAxisCombinationDPMFeedrateSettings.maximumFeedrate Property![](../images/TestTubeLarge.png)

Parent Object: [MultiAxisCombinationDPMFeedrateSettings](MultiAxisCombinationDPMFeedrateSettings.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisCombinationDPMFeedrateSettings.h>

## Description

The maximum feedrate value that can be output.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiAxisCombinationDPMFeedrateSettings\_var" is a variable referencing a MultiAxisCombinationDPMFeedrateSettings object. |

"multiAxisCombinationDPMFeedrateSettings\_var" is a variable referencing a MultiAxisCombinationDPMFeedrateSettings object. ```` ``` #include <Cam/Machine/MultiAxisCombinationDPMFeedrateSettings.h>  // Get the value of the property. double propertyValue = multiAxisCombinationDPMFeedrateSettings_var->maximumFeedrate();  // Set the value of the property, where value_var is a double. bool returnValue = multiAxisCombinationDPMFeedrateSettings_var->maximumFeedrate(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
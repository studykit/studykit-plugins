# ToolingCapabilitiesMachineElement.maxToolCount Property![](../images/TestTubeLarge.png)

Parent Object: [ToolingCapabilitiesMachineElement](ToolingCapabilitiesMachineElement.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/ToolingCapabilitiesMachineElement.h>

## Description

Property that represents the maximum number of tools available in the tool magazine, or the maximum number of tools that can be programmed in the control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolingCapabilitiesMachineElement\_var" is a variable referencing a ToolingCapabilitiesMachineElement object. |

"toolingCapabilitiesMachineElement\_var" is a variable referencing a ToolingCapabilitiesMachineElement object. ```` ``` #include <Cam/Machine/ToolingCapabilitiesMachineElement.h>  // Get the value of the property. integer propertyValue = toolingCapabilitiesMachineElement_var->maxToolCount();  // Set the value of the property, where value_var is an integer. bool returnValue = toolingCapabilitiesMachineElement_var->maxToolCount(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
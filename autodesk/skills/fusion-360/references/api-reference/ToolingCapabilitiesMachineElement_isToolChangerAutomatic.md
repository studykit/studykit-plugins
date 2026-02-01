# ToolingCapabilitiesMachineElement.isToolChangerAutomatic Property![](../images/TestTubeLarge.png)

Parent Object: [ToolingCapabilitiesMachineElement](ToolingCapabilitiesMachineElement.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/ToolingCapabilitiesMachineElement.h>

## Description

If your machine has an automatic tool changer, set this to true. For machines with manual tool change capabilities, set this to false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolingCapabilitiesMachineElement\_var" is a variable referencing a ToolingCapabilitiesMachineElement object. |

"toolingCapabilitiesMachineElement\_var" is a variable referencing a ToolingCapabilitiesMachineElement object. ```` ``` #include <Cam/Machine/ToolingCapabilitiesMachineElement.h>  // Get the value of the property. boolean propertyValue = toolingCapabilitiesMachineElement_var->isToolChangerAutomatic();  // Set the value of the property, where value_var is a boolean. bool returnValue = toolingCapabilitiesMachineElement_var->isToolChangerAutomatic(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
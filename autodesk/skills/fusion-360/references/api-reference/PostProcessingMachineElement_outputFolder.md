# PostProcessingMachineElement.outputFolder Property![](../images/TestTubeLarge.png)

Parent Object: [PostProcessingMachineElement](PostProcessingMachineElement.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/PostProcessingMachineElement.h>

## Description

Gets and sets the path for the output folder where the .nc files will be located.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postProcessingMachineElement\_var" is a variable referencing a PostProcessingMachineElement object. |

"postProcessingMachineElement\_var" is a variable referencing a PostProcessingMachineElement object. ```` ``` #include <Cam/Machine/PostProcessingMachineElement.h>  // Get the value of the property. string propertyValue = postProcessingMachineElement_var->outputFolder();  // Set the value of the property, where value_var is a string. bool returnValue = postProcessingMachineElement_var->outputFolder(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
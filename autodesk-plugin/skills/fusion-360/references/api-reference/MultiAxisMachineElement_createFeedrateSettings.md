# MultiAxisMachineElement.createFeedrateSettings Method![](../images/TestTubeLarge.png)

Parent Object: [MultiAxisMachineElement](MultiAxisMachineElement.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisMachineElement.h>

## Description

Creates a MultiAxisFeedrateSettings specialized object from the given input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiAxisMachineElement\_var" is a variable referencing a [MultiAxisMachineElement](MultiAxisMachineElement.htm) object.```` ``` returnValue = multiAxisMachineElement_var.createFeedrateSettings(input) ``` ```` |

"multiAxisMachineElement\_var" is a variable referencing a [MultiAxisMachineElement](MultiAxisMachineElement.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MultiAxisFeedrateSettings](MultiAxisFeedrateSettings.htm) | The specialized MultiAxisFeedrateSettings object created from the input. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MultiAxisFeedrateSettingsInput](MultiAxisFeedrateSettingsInput.htm) | The input object containing the settings to create the MultiAxisFeedrateSettings object. Set this object on the feedrateSettings property to apply the changes. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
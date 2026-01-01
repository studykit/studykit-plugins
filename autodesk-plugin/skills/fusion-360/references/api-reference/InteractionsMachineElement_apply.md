# InteractionsMachineElement.apply Method![](../images/TestTubeLarge.png)

Parent Object: [InteractionsMachineElement](InteractionsMachineElement.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/InteractionsMachineElement.h>

## Description

Add an MachineInteractionPair. This will overwrite any existing MachineInteractionPair with the same item1 and item2.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interactionsMachineElement\_var" is a variable referencing an [InteractionsMachineElement](InteractionsMachineElement.htm) object.```` ``` returnValue = interactionsMachineElement_var.apply(setting) ``` ```` |

"interactionsMachineElement\_var" is a variable referencing an [InteractionsMachineElement](InteractionsMachineElement.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| setting | [MachineInteractionPair](MachineInteractionPair.htm) |  |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
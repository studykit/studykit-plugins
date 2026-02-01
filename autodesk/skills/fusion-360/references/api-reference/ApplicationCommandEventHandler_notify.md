# ApplicationCommandEventHandler.notify Method

Parent Object: [ApplicationCommandEventHandler](ApplicationCommandEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEventHandler\_var" is a variable referencing an [ApplicationCommandEventHandler](ApplicationCommandEventHandler.htm) object.```` ``` returnValue = applicationCommandEventHandler_var.notify(eventArgs) ``` ```` |

"applicationCommandEventHandler\_var" is a variable referencing an [ApplicationCommandEventHandler](ApplicationCommandEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [ApplicationCommandEventArgs](ApplicationCommandEventArgs.htm) | The arguments object with details about this event and the firing ApplicationCommandEvent. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
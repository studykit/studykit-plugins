# InputChangedEventHandler.notify Method

Parent Object: [InputChangedEventHandler](InputChangedEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEventHandler\_var" is a variable referencing an [InputChangedEventHandler](InputChangedEventHandler.htm) object.```` ``` returnValue = inputChangedEventHandler_var.notify(eventArgs) ``` ```` |

"inputChangedEventHandler\_var" is a variable referencing an [InputChangedEventHandler](InputChangedEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [InputChangedEventArgs](InputChangedEventArgs.htm) | The arguments object with details about this event and the firing InputChangedEvent. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# DataEvent.add Method

Parent Object: [DataEvent](DataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEvent.h>

## Description

Add a handler to be notified when the data event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEvent\_var" is a variable referencing a [DataEvent](DataEvent.htm) object.```` ``` returnValue = dataEvent_var.add(handler) ``` ```` |

"dataEvent\_var" is a variable referencing a [DataEvent](DataEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [DataEventHandler](DataEventHandler.htm) | The handler object to be called when this event is fired. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Save and Insert File API Sample](SaveAndInsertSample_Sample.htm) | Demonstrates creating save a new file and then inserting it into a design. To use this sample, have a design open that has been saved and run the script. It will create a new design that contains a cylinder, save it to the same folder the active design was saved to, and then insert it into the active design. |

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
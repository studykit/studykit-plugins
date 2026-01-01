# MFGDMDataEvent.add Method

Parent Object: [MFGDMDataEvent](MFGDMDataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEvent.h>

## Description

Add a handler to be notified when the data event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEvent\_var" is a variable referencing a [MFGDMDataEvent](MFGDMDataEvent.htm) object.```` ``` returnValue = mFGDMDataEvent_var.add(handler) ``` ```` |

"mFGDMDataEvent\_var" is a variable referencing a [MFGDMDataEvent](MFGDMDataEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [MFGDMDataEventHandler](MFGDMDataEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
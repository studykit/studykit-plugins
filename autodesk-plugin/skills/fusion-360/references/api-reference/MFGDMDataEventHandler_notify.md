# MFGDMDataEventHandler.notify Method

Parent Object: [MFGDMDataEventHandler](MFGDMDataEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEventHandler\_var" is a variable referencing a [MFGDMDataEventHandler](MFGDMDataEventHandler.htm) object.```` ``` returnValue = mFGDMDataEventHandler_var.notify(eventArgs) ``` ```` |

"mFGDMDataEventHandler\_var" is a variable referencing a [MFGDMDataEventHandler](MFGDMDataEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [MFGDMDataEventArgs](MFGDMDataEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
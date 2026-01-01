# NavigationEventHandler.notify Method

Parent Object: [NavigationEventHandler](NavigationEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEventHandler\_var" is a variable referencing a [NavigationEventHandler](NavigationEventHandler.htm) object.```` ``` returnValue = navigationEventHandler_var.notify(eventArgs) ``` ```` |

"navigationEventHandler\_var" is a variable referencing a [NavigationEventHandler](NavigationEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [NavigationEventArgs](NavigationEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ApplicationEvent.name Property

Parent Object: [ApplicationEvent](ApplicationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEvent\_var" is a variable referencing an ApplicationEvent object. |

"applicationEvent\_var" is a variable referencing an ApplicationEvent object. ```` ``` #include <Core/Application/ApplicationEvent.h>  // Get the value of the property. string propertyValue = applicationEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
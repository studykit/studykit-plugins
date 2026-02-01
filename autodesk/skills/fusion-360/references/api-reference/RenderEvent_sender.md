# RenderEvent.sender Property

Parent Object: [RenderEvent](RenderEvent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEvent\_var" is a variable referencing a RenderEvent object. |

"renderEvent\_var" is a variable referencing a RenderEvent object. ```` ``` #include <Fusion/Render/RenderEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = renderEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
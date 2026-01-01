# RenderEventArgs.firingEvent Property

Parent Object: [RenderEventArgs](RenderEventArgs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object. |

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object. ```` ``` #include <Fusion/Render/RenderEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = renderEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
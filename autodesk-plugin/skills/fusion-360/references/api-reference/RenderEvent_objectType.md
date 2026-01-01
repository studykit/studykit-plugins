# RenderEvent.objectType Property

Parent Object: [RenderEvent](RenderEvent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEvent\_var" is a variable referencing a RenderEvent object.  ```` ``` # Get the value of the property. propertyValue = renderEvent_var.objectType ``` ```` |

"renderEvent\_var" is a variable referencing a RenderEvent object. ```` ``` #include <Fusion/Render/RenderEvent.h>  // Get the value of the property. string propertyValue = renderEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
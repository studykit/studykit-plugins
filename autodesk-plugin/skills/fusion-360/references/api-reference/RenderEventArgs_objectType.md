# RenderEventArgs.objectType Property

Parent Object: [RenderEventArgs](RenderEventArgs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object.  ```` ``` # Get the value of the property. propertyValue = renderEventArgs_var.objectType ``` ```` |

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object. ```` ``` #include <Fusion/Render/RenderEventArgs.h>  // Get the value of the property. string propertyValue = renderEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
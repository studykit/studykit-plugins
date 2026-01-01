# RenderFuture.objectType Property

Parent Object: [RenderFuture](RenderFuture.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderFuture.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderFuture\_var" is a variable referencing a RenderFuture object.  ```` ``` # Get the value of the property. propertyValue = renderFuture_var.objectType ``` ```` |

"renderFuture\_var" is a variable referencing a RenderFuture object. ```` ``` #include <Fusion/Render/RenderFuture.h>  // Get the value of the property. string propertyValue = renderFuture_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
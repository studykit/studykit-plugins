# RenderManager.objectType Property

Parent Object: [RenderManager](RenderManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderManager\_var" is a variable referencing a RenderManager object.  ```` ``` # Get the value of the property. propertyValue = renderManager_var.objectType ``` ```` |

"renderManager\_var" is a variable referencing a RenderManager object. ```` ``` #include <Fusion/Render/RenderManager.h>  // Get the value of the property. string propertyValue = renderManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
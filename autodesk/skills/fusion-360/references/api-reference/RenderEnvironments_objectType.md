# RenderEnvironments.objectType Property

Parent Object: [RenderEnvironments](RenderEnvironments.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEnvironments.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEnvironments\_var" is a variable referencing a RenderEnvironments object.  ```` ``` # Get the value of the property. propertyValue = renderEnvironments_var.objectType ``` ```` |

"renderEnvironments\_var" is a variable referencing a RenderEnvironments object. ```` ``` #include <Fusion/Render/RenderEnvironments.h>  // Get the value of the property. string propertyValue = renderEnvironments_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
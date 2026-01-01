# Rendering.objectType Property

Parent Object: [Rendering](Rendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/Rendering.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rendering\_var" is a variable referencing a Rendering object.  ```` ``` # Get the value of the property. propertyValue = rendering_var.objectType ``` ```` |

"rendering\_var" is a variable referencing a Rendering object. ```` ``` #include <Fusion/Render/Rendering.h>  // Get the value of the property. string propertyValue = rendering_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
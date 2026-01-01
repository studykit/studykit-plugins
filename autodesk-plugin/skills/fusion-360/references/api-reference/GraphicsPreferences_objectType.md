# GraphicsPreferences.objectType Property

Parent Object: [GraphicsPreferences](GraphicsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object.  ```` ``` # Get the value of the property. propertyValue = graphicsPreferences_var.objectType ``` ```` |

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. ```` ``` #include <Core/Application/GraphicsPreferences.h>  // Get the value of the property. string propertyValue = graphicsPreferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
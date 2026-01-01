# GraphicsPreferences.isValid Property

Parent Object: [GraphicsPreferences](GraphicsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. |

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. ```` ``` #include <Core/Application/GraphicsPreferences.h>  // Get the value of the property. boolean propertyValue = graphicsPreferences_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
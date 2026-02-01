# CustomGraphicsBRepBody.objectType Property

Parent Object: [CustomGraphicsBRepBody](CustomGraphicsBRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBRepBody.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBRepBody\_var" is a variable referencing a CustomGraphicsBRepBody object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsBRepBody_var.objectType ``` ```` |

"customGraphicsBRepBody\_var" is a variable referencing a CustomGraphicsBRepBody object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBRepBody.h>  // Get the value of the property. string propertyValue = customGraphicsBRepBody_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
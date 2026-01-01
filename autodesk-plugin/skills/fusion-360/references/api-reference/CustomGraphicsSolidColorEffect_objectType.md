# CustomGraphicsSolidColorEffect.objectType Property

Parent Object: [CustomGraphicsSolidColorEffect](CustomGraphicsSolidColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsSolidColorEffect.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsSolidColorEffect\_var" is a variable referencing a CustomGraphicsSolidColorEffect object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsSolidColorEffect_var.objectType ``` ```` |

"customGraphicsSolidColorEffect\_var" is a variable referencing a CustomGraphicsSolidColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsSolidColorEffect.h>  // Get the value of the property. string propertyValue = customGraphicsSolidColorEffect_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
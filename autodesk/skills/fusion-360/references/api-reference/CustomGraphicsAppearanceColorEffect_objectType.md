# CustomGraphicsAppearanceColorEffect.objectType Property

Parent Object: [CustomGraphicsAppearanceColorEffect](CustomGraphicsAppearanceColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsAppearanceColorEffect.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsAppearanceColorEffect\_var" is a variable referencing a CustomGraphicsAppearanceColorEffect object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsAppearanceColorEffect_var.objectType ``` ```` |

"customGraphicsAppearanceColorEffect\_var" is a variable referencing a CustomGraphicsAppearanceColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsAppearanceColorEffect.h>  // Get the value of the property. string propertyValue = customGraphicsAppearanceColorEffect_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CustomGraphicsBRepBody.name Property

Parent Object: [CustomGraphicsBRepBody](CustomGraphicsBRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBRepBody.h>

## Description

Gets and sets the name displayed when this entity is selected. If no name has been set, "Custom Graphics" will be displayed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBRepBody\_var" is a variable referencing a CustomGraphicsBRepBody object. |

"customGraphicsBRepBody\_var" is a variable referencing a CustomGraphicsBRepBody object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBRepBody.h>  // Get the value of the property. string propertyValue = customGraphicsBRepBody_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = customGraphicsBRepBody_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
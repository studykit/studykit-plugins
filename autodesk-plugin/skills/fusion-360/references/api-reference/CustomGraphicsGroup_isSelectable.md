# CustomGraphicsGroup.isSelectable Property

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Gets and sets if the graphics entity is selectable within the graphics window. By default, when a new entity is created it is selectable.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. |

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. ```` ``` #include <Fusion/Graphics/CustomGraphicsGroup.h>  // Get the value of the property. boolean propertyValue = customGraphicsGroup_var->isSelectable();  // Set the value of the property, where value_var is a boolean. bool returnValue = customGraphicsGroup_var->isSelectable(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CustomGraphicsPointSet.name Property

Parent Object: [CustomGraphicsPointSet](CustomGraphicsPointSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsPointSet.h>

## Description

Gets and sets the name displayed when this entity is selected. If no name has been set, "Custom Graphics" will be displayed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. |

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. ```` ``` #include <Fusion/Graphics/CustomGraphicsPointSet.h>  // Get the value of the property. string propertyValue = customGraphicsPointSet_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = customGraphicsPointSet_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
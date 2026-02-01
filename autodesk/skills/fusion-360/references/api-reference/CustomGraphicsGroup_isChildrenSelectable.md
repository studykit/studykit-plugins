# CustomGraphicsGroup.isChildrenSelectable Property

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Defines if the child custom graphic entities are selectable or if the entire group is selected in the UI. By default this is true. If false, the isSelectable property defines if this group is selectable. If true, the isSelectable property of each child entity defines if it is selectable.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. |

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. ```` ``` #include <Fusion/Graphics/CustomGraphicsGroup.h>  // Get the value of the property. boolean propertyValue = customGraphicsGroup_var->isChildrenSelectable();  // Set the value of the property, where value_var is a boolean. bool returnValue = customGraphicsGroup_var->isChildrenSelectable(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
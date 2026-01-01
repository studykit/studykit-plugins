# Component.material Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets and sets the physical material assigned to this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<Material> propertyValue = component_var->material();  // Set the value of the property, where value_var is a Material. bool returnValue = component_var->material(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Material](Material.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
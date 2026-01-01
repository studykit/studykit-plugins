# Component.description Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets and sets the description associated with this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. string propertyValue = component_var->description();  // Set the value of the property, where value_var is a string. bool returnValue = component_var->description(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
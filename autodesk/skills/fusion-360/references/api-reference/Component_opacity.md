# Component.opacity Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets and sets the opacity override assigned to this component. A value of 1.0 specifies that is it completely opaque and a value of 0.0 specifies that is it completely transparent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object.  ```` ``` # Get the value of the property. propertyValue = component_var.opacity  # Set the value of the property. component_var.opacity = propertyValue ``` ```` |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. double propertyValue = component_var->opacity();  // Set the value of the property, where value_var is a double. bool returnValue = component_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
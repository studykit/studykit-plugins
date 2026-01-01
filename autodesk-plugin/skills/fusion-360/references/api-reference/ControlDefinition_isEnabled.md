# ControlDefinition.isEnabled Property

Parent Object: [ControlDefinition](ControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ControlDefinition.h>

## Description

Gets or sets if this definition is enabled or not. This has the effect of enabling and disabling any associated controls.

## Syntax

* [Python](#Python)
* [C++](#C++)

"controlDefinition\_var" is a variable referencing a ControlDefinition object. |

"controlDefinition\_var" is a variable referencing a ControlDefinition object. ```` ``` #include <Core/UserInterface/ControlDefinition.h>  // Get the value of the property. boolean propertyValue = controlDefinition_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = controlDefinition_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
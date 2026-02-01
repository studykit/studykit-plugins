# CommandControl.isPromotedByDefault Property

Parent Object: [CommandControl](CommandControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandControl.h>

## Description

Gets or sets if this command is a default command in the panel. This defines the default state of the panel if the UI is reset. This property is ignored in the case where this control isn't in a panel.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandControl\_var" is a variable referencing a CommandControl object.  ```` ``` # Get the value of the property. propertyValue = commandControl_var.isPromotedByDefault  # Set the value of the property. commandControl_var.isPromotedByDefault = propertyValue ``` ```` |

"commandControl\_var" is a variable referencing a CommandControl object. ```` ``` #include <Core/UserInterface/CommandControl.h>  // Get the value of the property. boolean propertyValue = commandControl_var->isPromotedByDefault();  // Set the value of the property, where value_var is a boolean. bool returnValue = commandControl_var->isPromotedByDefault(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ButtonControlDefinition.name Property

Parent Object: [ButtonControlDefinition](ButtonControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ButtonControlDefinition.h>

## Description

Gets or sets the name for this control. This is the visible name displayed in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"buttonControlDefinition\_var" is a variable referencing a ButtonControlDefinition object. |

"buttonControlDefinition\_var" is a variable referencing a ButtonControlDefinition object. ```` ``` #include <Core/UserInterface/ButtonControlDefinition.h>  // Get the value of the property. string propertyValue = buttonControlDefinition_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = buttonControlDefinition_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
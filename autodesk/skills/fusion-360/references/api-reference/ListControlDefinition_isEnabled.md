# ListControlDefinition.isEnabled Property

Parent Object: [ListControlDefinition](ListControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListControlDefinition.h>

## Description

Gets or sets if this definition is enabled or not. This has the effect of enabling and disabling any associated controls.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. |

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. ```` ``` #include <Core/UserInterface/ListControlDefinition.h>  // Get the value of the property. boolean propertyValue = listControlDefinition_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = listControlDefinition_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
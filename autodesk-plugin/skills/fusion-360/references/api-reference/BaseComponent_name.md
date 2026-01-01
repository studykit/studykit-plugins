# BaseComponent.name Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Property that gets and sets the name of this component. This is the name shown in the browser for each occurrence referencing this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. string propertyValue = baseComponent_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = baseComponent_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# NamedView.name Property

Parent Object: [NamedView](NamedView.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedView.h>

## Description

Gets and sets the name of this named view. This property acts as read-only for the four standard named views. This can be determined by checking to see if the isBuiltIn property is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedView\_var" is a variable referencing a NamedView object. |

"namedView\_var" is a variable referencing a NamedView object. ```` ``` #include <Core/Application/NamedView.h>  // Get the value of the property. string propertyValue = namedView_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = namedView_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
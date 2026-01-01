# ContactSet.name Property

Parent Object: [ContactSet](ContactSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSet.h>

## Description

Gets and sets the name of the contact set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSet\_var" is a variable referencing a ContactSet object. |

"contactSet\_var" is a variable referencing a ContactSet object. ```` ``` #include <Fusion/Components/ContactSet.h>  // Get the value of the property. string propertyValue = contactSet_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = contactSet_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
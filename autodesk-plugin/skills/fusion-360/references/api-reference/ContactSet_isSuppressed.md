# ContactSet.isSuppressed Property

Parent Object: [ContactSet](ContactSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSet.h>

## Description

Gets and sets if this contact set is currently suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSet\_var" is a variable referencing a ContactSet object. |

"contactSet\_var" is a variable referencing a ContactSet object. ```` ``` #include <Fusion/Components/ContactSet.h>  // Get the value of the property. boolean propertyValue = contactSet_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = contactSet_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
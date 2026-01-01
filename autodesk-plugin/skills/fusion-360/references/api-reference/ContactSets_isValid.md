# ContactSets.isValid Property

Parent Object: [ContactSets](ContactSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSets.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSets\_var" is a variable referencing a ContactSets object. |

"contactSets\_var" is a variable referencing a ContactSets object. ```` ``` #include <Fusion/Components/ContactSets.h>  // Get the value of the property. boolean propertyValue = contactSets_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
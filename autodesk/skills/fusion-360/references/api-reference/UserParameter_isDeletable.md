# UserParameter.isDeletable Property

Parent Object: [UserParameter](UserParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameter.h>

## Description

Gets if this parameter can be deleted. Parameters that have dependents cannot be deleted, and model parameters typically cannot be deleted. However, there is the possibility in uncommon workflows where a model parameter no longer has any dependents, and it was not automatically deleted. In this case, this property will return true, and the deleteMe method can delete the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameter\_var" is a variable referencing a UserParameter object. |

"userParameter\_var" is a variable referencing a UserParameter object. ```` ``` #include <Fusion/Fusion/UserParameter.h>  // Get the value of the property. boolean propertyValue = userParameter_var->isDeletable(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ComponentList.objectType Property

Parent Object: [ComponentList](ComponentList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ComponentList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"componentList\_var" is a variable referencing a ComponentList object.  ```` ``` # Get the value of the property. propertyValue = componentList_var.objectType ``` ```` |

"componentList\_var" is a variable referencing a ComponentList object. ```` ``` #include <Fusion/Components/ComponentList.h>  // Get the value of the property. string propertyValue = componentList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
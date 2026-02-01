# Selections.all Property

Parent Object: [Selections](Selections.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selections.h>

## Description

Gets or sets all entities currently selected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selections\_var" is a variable referencing a Selections object. |

"selections\_var" is a variable referencing a Selections object. ```` ``` #include <Core/UserInterface/Selections.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = selections_var->all();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = selections_var->all(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
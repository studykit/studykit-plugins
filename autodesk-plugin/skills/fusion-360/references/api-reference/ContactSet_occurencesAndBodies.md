# ContactSet.occurencesAndBodies Property

Parent Object: [ContactSet](ContactSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSet.h>

## Description

Gets and sets the group of Occurrence and/or BRepBody objects that are part of this contact set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSet\_var" is a variable referencing a ContactSet object. |

"contactSet\_var" is a variable referencing a ContactSet object. ```` ``` #include <Fusion/Components/ContactSet.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = contactSet_var->occurencesAndBodies();  // Set the value of the property, where value_var is a Base. bool returnValue = contactSet_var->occurencesAndBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
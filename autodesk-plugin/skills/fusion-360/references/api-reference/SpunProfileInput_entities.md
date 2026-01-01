# SpunProfileInput.entities Property

Parent Object: [SpunProfileInput](SpunProfileInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SpunProfileInput.h>

## Description

Gets and sets the entities (BRepBody or BRepFace) used to define the shape of the spun profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. |

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. ```` ``` #include <Fusion/Sketch/SpunProfileInput.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = spunProfileInput_var->entities();  // Set the value of the property, where value_var is a Base. bool returnValue = spunProfileInput_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SpunProfileInput.axis Property

Parent Object: [SpunProfileInput](SpunProfileInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SpunProfileInput.h>

## Description

Gets and sets the entity used to define the axis of revolution. The axis can be a sketch line, construction axis, or linear edge. The axis must not be perpendicular to the sketch plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. |

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. ```` ``` #include <Fusion/Sketch/SpunProfileInput.h>  // Get the value of the property. Ptr<Base> propertyValue = spunProfileInput_var->axis();  // Set the value of the property, where value_var is a Base. bool returnValue = spunProfileInput_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
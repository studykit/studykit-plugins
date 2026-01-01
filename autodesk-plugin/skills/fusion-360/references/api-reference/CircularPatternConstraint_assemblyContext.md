# CircularPatternConstraint.assemblyContext Property

Parent Object: [CircularPatternConstraint](CircularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraint.h>

## Description

Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. |

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraint.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = circularPatternConstraint_var->assemblyContext(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
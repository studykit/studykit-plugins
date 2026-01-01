# Occurrence.fullPathName Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

The name of the occurrence, including the full path of occurrences as seen in the browser. The top-level component will depend on the context but will typically be the root component of the design. A name for an occurrence that is at the third level of an assembly could be "Sub1:1+Sub2:1+PartA:1".

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. string propertyValue = occurrence_var->fullPathName(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
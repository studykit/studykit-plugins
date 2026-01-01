# Analysis.attributes Property

Parent Object: [Analysis](Analysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analysis.h>

## Description

A property that returns the collection of attributes associated with this Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analysis\_var" is a variable referencing an Analysis object. |

"analysis\_var" is a variable referencing an Analysis object. ```` ``` #include <Fusion/Fusion/Analysis.h>  // Get the value of the property. Ptr<Attributes> propertyValue = analysis_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
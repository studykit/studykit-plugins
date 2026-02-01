# IsoCurveAnalysis.name Property

Parent Object: [IsoCurveAnalysis](IsoCurveAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IsoCurveAnalysis.h>

## Description

A property that gets and sets the name of the analysis. If you use a name that is not unique, Fusion will automatically append a number to the name to make it unique.

## Syntax

* [Python](#Python)
* [C++](#C++)

"isoCurveAnalysis\_var" is a variable referencing an IsoCurveAnalysis object. |

"isoCurveAnalysis\_var" is a variable referencing an IsoCurveAnalysis object. ```` ``` #include <Fusion/Fusion/IsoCurveAnalysis.h>  // Get the value of the property. string propertyValue = isoCurveAnalysis_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = isoCurveAnalysis_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
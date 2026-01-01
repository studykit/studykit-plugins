# Analysis.isVisible Property

Parent Object: [Analysis](Analysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analysis.h>

## Description

Gets if this Analysis is currently visible in the graphics window. The visibility is controlled by a combination of the isLightBulbOn properties of the Analyses collection object and the Analysis object. If both are true, the Analysis will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analysis\_var" is a variable referencing an Analysis object. |

"analysis\_var" is a variable referencing an Analysis object. ```` ``` #include <Fusion/Fusion/Analysis.h>  // Get the value of the property. boolean propertyValue = analysis_var->isVisible(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
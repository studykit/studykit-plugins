# Analysis.isLightBulbOn Property

Parent Object: [Analysis](Analysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analysis.h>

## Description

A property that gets and sets if the display is enabled for this Analysis object. If false, this analysis will be hidden. If true and the IsLightBulbOn property of the Analyses object is True the Analysis will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analysis\_var" is a variable referencing an Analysis object. |

"analysis\_var" is a variable referencing an Analysis object. ```` ``` #include <Fusion/Fusion/Analysis.h>  // Get the value of the property. boolean propertyValue = analysis_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = analysis_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
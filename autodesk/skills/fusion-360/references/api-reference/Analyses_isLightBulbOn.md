# Analyses.isLightBulbOn Property

Parent Object: [Analyses](Analyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analyses.h>

## Description

A property that gets and sets if the display is enabled for all Analysis objects in the design. If this is false, all Analysis results will be hidden. If this is true, the Analysis objects whose isLightBulbOn property is also true will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analyses\_var" is a variable referencing an Analyses object. |

"analyses\_var" is a variable referencing an Analyses object. ```` ``` #include <Fusion/Fusion/Analyses.h>  // Get the value of the property. boolean propertyValue = analyses_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = analyses_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |